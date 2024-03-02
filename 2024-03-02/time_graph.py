import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# csv 파일을 바탕으로 데이터프레임 생성 & 컬럼명 설정
df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-03-02/time_data.csv")
# df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-03-02/time_data.csv')
df.columns = ['Start', 'End']


# 문자열을 datetime object로 변경
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])


# y축 생성
y_labels = range(len(df))


# 그래프 사이즈 설정 & 폰트 사이즈 지정
plt.figure(figsize=(20, 6))
plt.rc('xtick', labelsize=5)


# 각 플롯의 시작점(시작 시간)과 가로 길이(소요 시간 만큼) 설정
left = df['Start']
width = df['End'] - df['Start']


# 막대 그래프 설정
plt.barh(y_labels, width, left=left, color='skyblue', edgecolor='black', alpha=0.8)


# x축 눈금 주기, 포맷(YYYY.MM.DD HH:MM), 스타일 설정
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y.%m.%d %H:%M'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.HourLocator(interval=6))
plt.xticks(rotation=45)


# 각 플롯의 시작 시간과 끝 시간을 그래프에 표기
for i, (start, end) in enumerate(zip(df['Start'], df['End'])):
    plt.text(start, i, start.strftime('%Y.%m.%d %H:%M'), fontsize=5, va='center', ha='right')
    plt.text(end, i, end.strftime('%Y.%m.%d %H:%M'), fontsize=5, va='center', ha='left')


# x축, y축 라벨 및 그래프 제목 설정
plt.xlabel('Time')
plt.ylabel('Data Index')
plt.title('Start Time and End Time for Each Data Entry')


# 그래프 생성 및 표출
plt.grid(axis='x')
plt.tight_layout()
plt.show()
