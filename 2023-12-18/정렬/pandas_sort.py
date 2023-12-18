import pandas as pd

# 리스트 생성
lst = [
  ['David', 72],
  ['Sam', 98],
  ['Sarah', 92],
  ['Peter', 90]
]

# 리스트를 바탕으로 데이터프레임 생성
df = pd.DataFrame(lst)
df.columns = ['Name', 'Score']
df.index = [i for i in range(1, len(lst)+1)]

# 데이터프레임 출력
print(df)
print()

# 성적 기준으로 정렬 후 출력
df = df.sort_values(by='Score', ascending = False)
print(df)
