# build a series that returns S00 Red, S01 Green, S02 White, S10 Red, S11 Black, S20 Yelloe
import pandas as pd
d = {0: ['Red', 'Green', 'White'], 1: ['Red', 'Black'], 2: ['Yellow']}

labels = ["S" + str(key) + str(i) for key, values in d.items() for i in range(len(values))]
values = [color for values in colori.values() for color in values]
colori_series = pd.Series(values, index = labels)
print(colori_series)
