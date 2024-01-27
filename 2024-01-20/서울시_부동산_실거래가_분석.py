import pandas as pd
import matplotlib.pyplot as plt

# 경고 무시
import warnings
warnings.filterwarnings('ignore')

# 데이터 로드
df = pd.read_csv('data.csv')

# 결측치 제거
df.fillna('-')
print(df.head())

# 건물 용도별로 묶기
df = df.sort_values(by='건물용도')
df.index = [i for i in range(len(df.index))]
# print(df.head(500))

# 아파트 관련 데이터 추출
start = -1
end = 0

for i in range(len(df.index)):
    if start == -1 and df['건물용도'][i] == '아파트':
        start = i
    elif start != -1 and df['건물용도'][i] != '아파트':
        end = i
        break

apartment = df[start:end]

# 자치구별로 묶기
apartment = apartment.sort_values(by='자치구명')
# print(apartment)

# 자치구별 아파트 실거래가 정보 추출
# print(apartment.groupby('자치구명').mean())
print(apartment.grouby('자치구명').mean()['물건금액(만원)'])


# 예산에 맞는 아파트 찾기
budget = int(input('예산 입력 : '))
apartment = apartment.sort_values(by='물건금액(만원)', ascending=True)
apartment.index = [i for i in range(len(df.apartment))]

threshold = 0

for i in range(len(apartment.index)):
    if apartment['물건금액(만원)'][i] > budget:
        threshold = i
        break

print(apartment.head(threshold-1))
