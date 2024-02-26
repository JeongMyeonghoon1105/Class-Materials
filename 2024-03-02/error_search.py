import pandas as pd


df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-03-02/data.csv')


error = '서울'

for i in range(len(df.index)):
  text = ''
  index = 0
  prev = 0

  while index <= len(df['0'][i]):
    condition_set = [False, False, False, False]

    while False in condition_set:
      print(condition_set)
      print(df['0'][i][index])
      if df['0'][i][index] == '(':
        condition_set[0] = True
      if condition_set[0] and df['0'][i][index] == ':':
        condition_set[1] = True
      if condition_set[0] and condition_set[1] and df['0'][i][index] == ':':
        condition_set[2] = True
      if condition_set[0] and condition_set[1] and condition_set[2] and df['0'][i][index] == ')':
        condition_set[3] = True
      index += 1
    
    if error not in df['0'][i][prev:index]:
      text += df['0'][i][prev:index]
    
    prev = index

  df['0'][i] = text

print(df)
