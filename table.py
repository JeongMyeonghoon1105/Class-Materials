import pandas as pd

def find(c):
    index = 0
    while True:
        start = input('기준월이 시작되는 요일을 입력하세요: ')
        for i, c in enumerate(c):
            if c == start:
                index = i
                return index

names = ['김사랑', '이사랑', '정사랑', '오사랑', '유사랑', '지사랑', '표사랑']
calender = ['월', '화', '수', '목', '금', '토', '일']

index = find(calender)

end = 0
while True:
    end = int(input('기준월의 마지막 날짜를 입력하세요(ex. 28, 29, 30, 31): '))
    if 1 <= end <= 31:
        break

while True:
    default = input('기준월 1조의 평일 근무 형태를 입력하세요(ex. A, B): ')
    if default == 'A' or default == 'B':
        break

lst = []
for i in range(1, end+1):
    lst.append(calender[index])
    if index >= 6:
        index = 0
    else:
        index += 1

table = [
    ['요일'] + lst
]

for i in range(len(names)):
    table += [[names[i]] + ['' for i in range(end)]]

brk = [0, 1]
brk_index = 0
prev1, prev2 = input('2주 전 주말에 휴무였던 사람 두 명의 이름을 띄어쓰기로 구분하여 입력하세요: ').split()
for i, prev_name in enumerate(names):
    if prev1 == prev_name or prev2 == prev_name:
        brk_index = i
        break

for i in range(1, len(names)+1):
    status = default
    for j in range(1, end+1):
        if table[0][j] != '토' and table[0][j] != '일':
            table[i][j] = status
        # 주말일 때
        else:
            # 휴무자 표시
            # 휴무자 번호 증가시키기
            # 지지난주 주말 휴무자 중 윗 사람 C 근무 배정
            # 근무자 위 두 명 토요일 D 근무 배정
            # 나머지 두 명 일요일 D 근무 배정


            if table[0][j] == '토':
                if status == 'B':
                    status = 'A'
                else:
                    status = 'B'
        

team1 = pd.DataFrame(table)
team1.columns = ['날짜'] + [i for i in range(1, end+1)]
team1.to_csv('team1.csv')

print(team1)
