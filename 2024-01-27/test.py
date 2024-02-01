import pandas as pd
from datetime import timedelta as td

# df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-01-27/data.csv")
df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-01-27/data.csv')
a = pd.DataFrame([], columns = df.columns)
b = pd.DataFrame([], columns = df.columns)
c = pd.DataFrame([], columns = df.columns)

for i in range(len(df.index)):
    if df['PH'][i][0] == 'E':
        a.loc[len(a.index)] = df.loc[i]
    if 'KR' in df['jkl'][i] or df['PH'][i][0] == 'M':
        b.loc[len(b.index)] = df.loc[i]
    if 'AR' in df['jkl'][i]:
        c.loc[len(c.index)] = df.loc[i]

lst = []
for i in range(len(a.index)):
    diff = pd.to_datetime(df['ghi'][i]) - pd.to_datetime(df['def'][i])
    lst.append(diff.days * 24 + diff.seconds // 3600)
print(lst)
a['test'] = lst


# print(df.columns)
# print()
print(a)
# print()
# print(b)
# print()
# print(c)
# print()


a.to_csv('a.csv', index=False)
# b.to_csv('b.csv', index=False)
# c.to_csv('c.csv', index=False)
