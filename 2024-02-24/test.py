import pandas as pd
from datetime import timedelta as td


df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-02-24/data.csv")
# df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-01-27/data.csv')


lst = []
for i in range(len(df.index)):
    if '조건1' in df['컬럼1'][i] and df['컬럼2'][i] == '조건2':
        lst.append('작업1')
    elif '조건3' in df['컬럼3'][i] and df['컬럼4'][i] == '조건4':
        lst.append('작업2')
df['새 컬럼 이름'] = lst


# 추후 계산을 위해 시간 데이터를 저장할 리스트
savings = []
# 데이터프레임에 붙여넣을 문자형 시간 데이터를 담을 리스트
lst = []

for i in range(len(df.index)):
    # 시간차 계산하여 날짜 & 초 단위로 나타내기
    diff = pd.to_datetime(df['ghi'][i]) - pd.to_datetime(df['def'][i])
    # 날짜 & 초 --> 시간 & 분으로 바꾸어 savings(계산용)에 저장
    savings.append([diff.days * 24 + diff.seconds // 3600, (diff.seconds % 3600) // 60])
    # 날짜 & 초 --> 시간:분으로 바꾼 데이터를 문자형으로 바꾸어 lst에 저장
    lst.append(str(savings[i][0]) + ':' + str(savings[i][1]))

# 시간:분 문자 데이터가 담긴 리스트를 데이터프레임의 새로운 열로 붙이기
df['New Column 2'] = lst


# 특정 조건 두 가지를 만족하는 데이터의 개수를 저장할 변수
count = 0
# 특정 조건 두 가지를 만족하는 데이터의 시간차를 저장할 리스트
# 0번: 시간, 1번: 분
time_diff = [0, 0]

# 특정 조건 두 가지를 만족하는 데이터의 개수 세기
# 특정 조건 두 가지를 만족하는 데이터의 시간차 계산하여 누적하기
for i in range(len(df.index)):
    if '조건1' in df['컬럼 이름1'][i] and '조건2' in df['컬럼 이름2'][i]:
        # 조건을 만족하는 건수 세기
        count += 1
        # 시간차 계산(날짜 & 초 단위)
        diff = pd.to_datetime(df['나중 시간 저장한 컬럼 이름'][i]) - pd.to_datetime(df['먼저 시간 저장한 컬럼 이름'][i])
        # 시간 계산(날짜 & 초에서 시간 뽑아내기)
        time_diff[0] += diff.days * 24 + diff.seconds // 3600
        # 분 계산(날짜 & 초에서 분 뽑아내기)
        time_diff[1] += (diff.seconds % 3600) // 60

# 출력
print('조건1 및 조건2 만족\t' + str(count) + '건\t' + str(time_diff[0]) + ':' + str(time_diff[1]))

# 별도의 엑셀 파일로 분리
df2 = pd.DataFrame(['조건1', '조건2', count, str(time_diff[0]) + ':' + str(time_diff[1])])
df2.to_csv('result.csv', index=False)
