import pandas as pd
import random as rd
import warnings
warnings.filterwarnings(action='ignore')

overlap = []
lst = [
  ['David', 0],
  ['Sam', 0],
  ['Sarah', 0],
  ['Peter', 0],
  ['Esther', 0],
  ['Paul', 0],
  ['Josh', 0]
]

df = pd.DataFrame(lst)
df.columns = ['Name', 'Order']
df.index = [i for i in range(1, len(lst)+1)]
print(df)
print()

for i in range(1, len(df.index)+1):
  while True:
    rand_num = rd.randrange(1, 8)
    if rand_num not in overlap:
      break
  df['Order'][i] = rand_num
  overlap.append(rand_num)

df = df.sort_values(by='Order', ascending = True)
print(df)
