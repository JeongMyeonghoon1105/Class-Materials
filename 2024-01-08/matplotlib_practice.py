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
# plt.plot([1, 2, 3, 4, 5], [2, 5, 7, 9, 10], 'g--', linewidth=5, markersize = 12)
# plt.show()

# 막대 그래프
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 10]
plt.bar(x, y)
plt.show()

# 여러 개의 그래프 그리기
# lst = [
#     [1, 2, 3, 4, 5],
#     [3, 5, 7, 9, 10],
#     [2, 4, 8, 6, 12],
#     [5, 10, 12, 13, 17]
# ]
# plt.plot(lst[0], lst[1], 'b-', lst[0], lst[2], 'g-', lst[0], lst[3], 'r-')
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
# import pandas as pd

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

# plt.plot(df.index.to_list(), df['David'].to_list(), 'b-')
# plt.xlabel('Month')
# plt.ylabel('Score')
# plt.show()