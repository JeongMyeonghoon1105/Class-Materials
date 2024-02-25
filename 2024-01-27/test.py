import pandas as pd
from datetime import timedelta as td


<<<<<<< HEAD
# csv 파일 불러와서 데이터프레임 생성
# df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-01-27/data.csv")
df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-01-27/data.csv')

# a, b, c 데이터프레임 생성
=======
df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-01-27/data.csv")
# df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-01-27/data.csv')
>>>>>>> 27ee084523da7045818f7b0ff60aebc2e219f813
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

<<<<<<< HEAD

# ghi 컬럼과 def 컬럼의 차(시간 단위) 계산하여 'test'라는 이름의 새 컬럼 생성
lst = []
for i in range(len(a.index)):
    diff = pd.to_datetime(df['ghi'][i]) - pd.to_datetime(df['def'][i])
    # 두 컬럼의 차이를 계산하면 날짜 및 시간으로 이루어진 timedelta 값이 나옴
    # (날짜 * 24 + 초 / 3600)의 값을 통해 시간차 계산
    lst.append(diff.days * 24 + diff.seconds // 3600)
=======
a_lst = []
lst = []
for i in range(len(a.index)):
    diff = pd.to_datetime(a['ghi'][i]) - pd.to_datetime(a['def'][i])
    a_lst.append([diff.days * 24 + diff.seconds // 3600, (diff.seconds % 3600) // 60])
    lst.append(str(a_lst[i][0]) + ':' + str(a_lst[i][1]))
>>>>>>> 27ee084523da7045818f7b0ff60aebc2e219f813
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

<<<<<<< HEAD
# 각 데이터프레임을 csv 파일로 저장
=======
print(a)
print()
print(b)
print()
print(c)
print()


>>>>>>> 27ee084523da7045818f7b0ff60aebc2e219f813
a.to_csv('a.csv', index=False)
b.to_csv('b.csv', index=False)
c.to_csv('c.csv', index=False)
