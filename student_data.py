import pandas as pd
df = pd.read_csv("~/Downloads/student_data.csv", index_col = 0)

for names, groups in df.groupby('school_code'):
    print(names)
    print(groups)

df.groupby('school_code')[['age', 'height', 'weight']].mean()

functions = ["min", "max", "mean"]
school_names['age'].agg(functions)


for names, groups in df.groupby(['school_code', 'class']):
    print(names)
    print(groups)

groups = list()
for school_names, x in df.groupby('school_code'):
    groups.append(x)

df.groupby(['school_code']).size()

grouped = df.groupby('school_code')
pd.concat([grouped.get_group('s001'), grouped.get_group('s004')])

grouped = df.groupby('school_code')
filtered_groups = grouped.filter(lambda x: x.name in ['s001', 's004'])

df.groupby(["school_code", "class"]).agg({"age": ["min", "max", "mean"],
                                          "weight": "sum"})

def get_stats(group):
    # Use the group name (school_code) as the index for the DataFrame
    return pd.DataFrame(
        {"avg_age": [group['age'].mean()],
         "age_max": [group['age'].max()],
         "age_min": [group['age'].min()]},
        index=[group.name]  # Use the group name as the index
    )

df.groupby('school_code').apply(get_stats).reset_index()

school_names = df.groupby('school_code').agg(
    avg_age = ('age', 'mean'),
    age_max = ('age', 'max'),
    age_min = ('age', 'min')
)

# Calcolare il bmi
df['bmi'] = (df['weight'] / (df['height'] /100) **2)
df.groupby("school_code")["bmi"].mean()


