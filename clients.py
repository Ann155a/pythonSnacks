df = pd.read_csv("~/Downloads/order_data.csv", index_col = 0)

#1. Per ogni cliente, calcola l'acquisto minimo, medio e massimo  
df_1 = df.groupby("customer_id").agg({"purch_amt": ["min", "max", "mean"]})
df_1 = df.groupby("customer_id").agg(
    purch_amt_min = ('purch_amt', 'min'),
    purch_amt_max = ('purch_amt', 'max'),
    purch_amt_mean = ('purch_amt', 'mean')
)

# 2. approfondite la funzione to_datetime, quando e' stato l'ultimo acquisto. converte l'oggetto in una data, acceddere con dt 
df['ord_date'] = pd.to_datetime(df['ord_date'])
df_2 = df.groupby('customer_id')['ord_date'].max()

# 3. Calcolare la frequenza di acquisto
df_3 = df.groupby('customer_id').size()

# 4. Definire un dataframe che rappresenti con i fattori RFM per cliente
# Merge df_1 and df_2 on 'customer_id'
df_RFM = pd.merge(df_1, df_2, on = 'customer_id', how ='inner')

# Merge the result with df_3 on 'customer_id'
df_RFM = pd.merge(df_RFM, df_3, on = 'customer_id', how = 'inner')

