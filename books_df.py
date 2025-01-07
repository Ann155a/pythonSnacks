df = pd.read_csv("~/Downloads/BL-Flickr-Images-Book.csv")

# Drop columns 
df.columns.tolist() # prendiamo l'elenco di colonne
df = df.drop(columns = ['Edition Statement', 
                        'Corporate Author',  
                        'Corporate Contributors', 
                        'Former owner', 
                        'Contributors',  
                        'Issuance type', 
                        'Shelfmarks'])

# Identifier: indici di variabili unici. 
df['Identifier'].is_unique
df.set_index('Identifier', inplace = True)

# Le prime 10 righe a partire dalla righa 1905, e in particolare la colonna, 'Date of Publication'
df['Date of Publication'].loc[1905:].head(10)

# Anno dal colonna Date of Publication
df['Date of Publication'] = df['Date of Publication'].str.extract('(\d{4})')
df['Date of Publication'] = df['Date of Publication'].str.extract('([0-9]{4})') #piu' efficiente

# Convertite la colonna in numerica
df['Date of Publication'] = pd.to_numeric(df['Date of Publication'])

# Trova la % di nan
df['Date of Publication'].isna().sum()
df['Date of Publication'].isna().sum()/len(df['Date of Publication'])*100


# Avere london se compare london, oxford se compare oxford, altro. Creo un altra colonna e la sostituisco
df['Location'] = df['Place of Publication'].apply(
    lambda x: "London" if "London" in x else 
    "Oxford" if "Oxford" in x else
    "Other")


