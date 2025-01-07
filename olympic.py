# Olympic database
### Database olimpico
#1. Ridenominare le colonne
#2. Togliere le colonne derivate
#3. Se vedete country, fatte (AFG) indice di riga.
#4. Quale nazione ha vinto di piu in relazione al numero di olimpiadi cui ha partecipato. Bronze 50%, silver = 75% e gold 100%

import pandas as pd
import re
 
# La lista di nomi associati alle colonne
column_name = ["state", "summer", "goldS", "silverS", "bronzeS", "totalS",
                                       "winter", "goldW", "silverW", "bronzeW", "totalW",
                                       "games", "goldG", "silverG", "bronzeG", "combinedTotal"]
# Carico il file csv
df = pd.read_csv('/home/anisa_bakiu/Downloads/olympics.csv', skiprows = {0,1}, names = column_name)
 
# Controllo se `skiprow` ha funzionato correttamente e se ci sono anche righe da togliere
df.head()
df.tail()
 
# Elenco di colonne derivate
list2drop = ["games", "goldG", "silverG", "bronzeG", "combinedTotal"]
 
# Li togliamo dal dataset
df.drop(list2drop, axis = 1, inplace = True)
 
# Provvedo ad eliminare anche l'ultima riga che contiene il totale di colonne siccome e' derivata e inutile ai fini delle analisi
df.drop(df.index[-1], axis = 0, inplace = True)
 
# Calcolo l'indice di successo per ogni squadra
df['ind_successo'] = (
    ((df['goldS'] + df['goldW']) * 1 +
     (df['silverS'] + df['silverW']) * 0.75 +
     (df['bronzeS'] + df['bronzeW']) * 0.5) /
    (df['summer'] + df['winter'])
)
 
# Trovo quale squadra ha l'indice maggiore
df.iloc[df['ind_successo'].idxmax(), [0, -1]]
 
# Il risultato non sembra uno stato pertanto stampo le prime 10 squadre per capire meglio
df.sort_values(by = 'ind_successo', ascending = False).head(10)
 
# Individuo l'indice per ogni stato e intanto aggiungo la colonna chiamata 'codice'
df['codice'] = df['state'].apply(lambda x: re.findall(r"\((.*?)\)", x))
 
# che sara' il nuovo indice del dataframe
df.set_index('codice', inplace = True)
 
# Per togliere gli indici dalla colonna degli stati, mantengo solo la parte prima delle parentesi
df['state'] = df['state'].apply(lambda x: re.search(r"^(.*?)\s*\(", x).group(1))
 
# Confermo se il dataframe soddisfa le condizioni 
df
