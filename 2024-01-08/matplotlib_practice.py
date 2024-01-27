# 설치 
# python -m pip install -U pip
# python -m pip install -U matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# y값 그래프
# plt.plot([2, 5, 7, 9, 10])
# plt.show()
 
# x, y값 그래프
# plt.plot([1, 2, 3, 4, 5], [2, 5, 7, 9, 10])
# plt.show()

# Format String
# https://matplotlib.org/3.4.3/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
# ro, bo, g-, b-- 등
# plt.plot([1, 2, 3, 4, 5], [2, 5, 7, 9, 10], 'go')
# plt.show()

# 막대 그래프
# x = [1, 2, 3, 4, 5]
# y = [3, 5, 7, 9, 10]
# plt.bar(x, y)
# plt.show()

# 여러 개의 그래프 그리기
# x = [1, 2, 3, 4, 5]
# y1 = [3, 5, 7, 9, 10]
# y2 = [2, 4, 8, 6, 12]
# y3 = [5, 10, 12, 13, 17]

# plt.plot(x, y1, 'b-', x, y2, 'g-', x, y3, 'r-')
# plt.show()

# 각 축에 label name 넣기
# lst = [
#     ['1/1', '2/1', '3/1', '4/1', '5/1'],
#     [3, 5, 7, 9, 10],
#     [2, 4, 8, 6, 12],
#     [5, 10, 12, 13, 17]
# ]
# plt.plot(lst[0], lst[1], 'b-', lst[0], lst[2], 'g-', lst[0], lst[3], 'r-')
# plt.xlabel('Month')
# plt.ylabel('Output')
# plt.show()

# 데이터프레임 시각화
# lst = [
#     [50, 60, 70, 80],
#     [62, 63, 55, 77],
#     [73, 72, 55, 66],
#     [72, 83, 55, 67],
#     [76, 71, 45, 36],
# ]

# df = pd.DataFrame(lst)
# df.index = ['1/1', '2/1', '3/1', '4/1', '5/1']
# df.columns = ['David', 'Joshua', 'Aaron', 'Phillip']
# print(df)

# plt.plot(df.index, df['David'].to_list(), 'b-')
# plt.xlabel('Month')
# plt.ylabel('Score')
# plt.show()

# 실생활 데이터 시각화
df = pd.read_csv('C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-01-08/data.csv', engine='python')

# 중앙탑면의 총 인구 구하기
# for i in range(len(df.index)):
#     if (df['구분'][i] == '중앙탑면'):
#         print(df['총인구(계)'][i])
#         break

# 각 읍면동별 인구 막대그래프 그리기
import matplotlib.font_manager as fm
font_path = 'C:/Windows/Fonts/gulim.ttc'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.bar(df['구분'].to_list(), df['총인구(계)'].to_list())
plt.show()
