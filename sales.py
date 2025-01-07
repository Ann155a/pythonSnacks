df = pd.read_csv("~/Downloads/sales_data.csv", index_col = 0)

# 1. calcolare la media delle vendite per stagione. ID, media per ogni stagione
mapping = {"spring": ["sale_mar", "sale_apr", "sale_may"],
           "summer": ["sale_jun", "sale_jul", "sale_aug"],
           "autumn": ["sale_sep", "sale_oct", "sale_nov"],
            "winter": ["sale_dec", "sale_jan", "sale_feb"]}
# Calcoliamo la media per ogni stagione
for mapping, mese in seasons.items():
    df[mapping] = df[mese].mean(axis=1)

df[["salesman_id", "sale_winter", "sale_spring", "sale_summer", "sale_autumn"]]

month_to_season = {
    "sale_jan": "winter",
    "sale_feb": "winter",
    "sale_dec": "winter",
    "sale_mar": "spring",
    "sale_apr": "spring",
    "sale_may": "spring",
    "sale_jun": "summer",
    "sale_jul": "summer",
    "sale_aug": "summer",
    "sale_sep": "autumn",
    "sale_oct": "autumn",
    "sale_nov": "autumn",
}

df_transposed = df.set_index("salesman_id").T  
df_transposed["season"] = df_transposed.index.map(month_to_season)  

seasonal_means = df_transposed.groupby("season").mean().T  

seasonal_means = seasonal_means.reset_index()
seasonal_means.rename(columns={"index": "salesman_id"}, inplace=True)

# Opzione: Per ciascun cliente dovete indicare la stagione in cui e' piu' prolifico
seasonal_means["most_revenue"] = seasonal_means[["winter", "spring", "summer", "autumn"]].idxmax(axis = 1)
seasonal_means[["salesman_id", "most_revenue"]]

