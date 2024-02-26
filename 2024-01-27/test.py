import pandas as pd
from datetime import timedelta as td


# csv 파일 불러와서 데이터프레임 생성
# df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-01-27/data.csv")
df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-01-27/data.csv')

# a, b, c 데이터프레임 생성
a = pd.DataFrame([], columns = df.columns)
b = pd.DataFrame([], columns = df.columns)
c = pd.DataFrame([], columns = df.columns)


# 조건에 따라 데이터 분류하여 a, b, c 데이터프레임에 저장
for i in range(len(df.index)):
    if df['PH'][i][0] == 'E':
        a.loc[len(a.index)] = df.loc[i]
    if 'KR' in df['jkl'][i] or df['PH'][i][0] == 'M':
        b.loc[len(b.index)] = df.loc[i]
    if 'AR' in df['jkl'][i]:
        c.loc[len(c.index)] = df.loc[i]

a_lst = []
lst = []
for i in range(len(a.index)):
    diff = pd.to_datetime(a['ghi'][i]) - pd.to_datetime(a['def'][i])
    a_lst.append([diff.days * 24 + diff.seconds // 3600, (diff.seconds % 3600) // 60])
    lst.append(str(a_lst[i][0]) + ':' + str(a_lst[i][1]))
a['test'] = lst

h_sum = 0
m_sum = 0
for i in range(len(a_lst)):
    h_sum += a_lst[i][0]
    m_sum += a_lst[i][1]
a.loc[len(a.index)] = ['' for i in range(len(a.columns)-1)] + [str(h_sum // len(a_lst)) + ':' + str(m_sum // len(a_lst))]




b_lst = []
lst = []
for i in range(len(b.index)):
    diff = pd.to_datetime(b['ghi'][i]) - pd.to_datetime(b['def'][i])
    b_lst.append([diff.days * 24 + diff.seconds // 3600, (diff.seconds % 3600) // 60])
    lst.append(str(b_lst[i][0]) + ':' + str(b_lst[i][1]))
b['test'] = lst

h_sum = 0
m_sum = 0
for i in range(len(b_lst)):
    h_sum += b_lst[i][0]
    m_sum += b_lst[i][1]
b.loc[len(b.index)] = ['' for i in range(len(b.columns)-1)] + [str(h_sum // len(b_lst)) + ':' + str(m_sum // len(b_lst))]




c_lst = []
lst = []
for i in range(len(c.index)):
    diff = pd.to_datetime(c['ghi'][i]) - pd.to_datetime(c['def'][i])
    c_lst.append([diff.days * 24 + diff.seconds // 3600, (diff.seconds % 3600) // 60])
    lst.append(str(c_lst[i][0]) + ':' + str(c_lst[i][1]))
c['test'] = lst

h_sum = 0
m_sum = 0
for i in range(len(c_lst)):
    h_sum += c_lst[i][0]
    m_sum += c_lst[i][1]
c.loc[len(c.index)] = ['' for i in range(len(c.columns)-1)] + [str(h_sum // len(c_lst)) + ':' + str(m_sum // len(c_lst))]

print(a)
print()
print(b)
print()
print(c)
print()


a.to_csv('a.csv', index=False)
b.to_csv('b.csv', index=False)
c.to_csv('c.csv', index=False)
