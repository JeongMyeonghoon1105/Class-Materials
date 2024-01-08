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

# 여러 개의 그래프 그리기
lst = [
    [1, 2, 3, 4, 5],
    [3, 5, 7, 9, 10],
    [2, 4, 8, 6, 12],
    [5, 10, 12, 13, 17]
]
plt.plot(lst[0], lst[1], 'b-', lst[0], lst[2], 'g-', lst[0], lst[3], 'r-')
plt.show()
