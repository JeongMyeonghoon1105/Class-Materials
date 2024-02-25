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


# ghi 컬럼과 def 컬럼의 차(시간 단위) 계산하여 'test'라는 이름의 새 컬럼 생성
lst = []
for i in range(len(a.index)):
    diff = pd.to_datetime(df['ghi'][i]) - pd.to_datetime(df['def'][i])
    # 두 컬럼의 차이를 계산하면 날짜 및 시간으로 이루어진 timedelta 값이 나옴
    # (날짜 * 24 + 초 / 3600)의 값을 통해 시간차 계산
    lst.append(diff.days * 24 + diff.seconds // 3600)
a['test'] = lst


# 각 데이터프레임을 csv 파일로 저장
a.to_csv('a.csv', index=False)
b.to_csv('b.csv', index=False)
c.to_csv('c.csv', index=False)
