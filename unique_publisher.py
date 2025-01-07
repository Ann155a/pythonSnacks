# Extract unique, ordinal publishers for the frequency that occurs within the dataframe. 
# It is likely that the rarest ones are not actually different, 
# but it could be publishers that are poorly written.

publisher_counts = df['Publisher'].value_counts()
unique_publishers = publisher_counts[publisher_counts == 1].index.tolist()

# Definisco la funzione simple similarity: (case-insensitive comparison)
def simple_similarity(str1, str2):
    # Normalizzo in lowercase 
    str1, str2 = str1.lower(), str2.lower()
    # Calcola il numero di caratteri uguali
    matches = sum(1 for c1, c2 in zip(str1, str2) if c1 == c2)
    # Calcola la percentuale di caratteri uguali
    return (matches / max(len(str1), len(str2))) * 100

# Ragruppa publisher uguali
groups = {}

for publisher in unique_publishers:
    matched = False
    for key in groups:
        # Comparazione di valori
        if simple_similarity(publisher, key) > 90:  # soglia di similita'
            groups[key].append(publisher)
            matched = True
    if not matched:
        # Crea un altro gruppo se non si trova nessun nome simile
        groups[publisher] = [publisher]

# Fai vedere i gruppi
for group, members in groups.items():
    if len(members) > 1:  # Solo gruppi non valori unici
        print(f"Group: {group} -> Variants: {members}")
