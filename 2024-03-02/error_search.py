import pandas as pd


df = pd.read_csv("C:/Users/Coding Lab/Desktop/Data-Analysis-Class/2024-03-02/data.csv")
# df = pd.read_csv('/Users/jeongmyeonghun/Desktop/학원 수업/2024-03-02/data.csv')


error = '서울'
data = []

for i in range(len(df.index)):
  prev = 0
  index = 0
  stack = []

  for j in range(len(df['1'][i])):
    if df['1'][i][j] == '(':
      stack.append('(')
    elif df['1'][i][j] == ':':
      if stack:
        if stack[-1] == '(' or stack[-1] == ':' and stack[-2] == '(':
          stack.append(':')
    elif df['1'][i][j] == ')':
      if stack:
        if stack[-1] == '(':
          stack.pop()
        elif stack[-1] == ':':
          index = j
          if error not in df['1'][i][prev:index+1]:
            data.append([df['0'][i], df['1'][i][prev:index+1]])
          prev = index+1

result = pd.DataFrame(data)
result.to_csv('result.csv', index=False)
