# 기준월이 일요일부터 시작할 때
# 휴무였던 사람이 마지막이랑 첫번째일 경우


import pandas as pd

# 시작 요일이 요일을 저장하는 리스트의 몇 번째 칸에 위치하는지
# ex. '목'을 입력하면 인덱스인 3을 리턴
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

# 기준월의 마지막 날짜를 입력받기
# 잘못된 입력을 할 시 다시 입력하도록 함
end = 0
while True:
    end = int(input('기준월의 마지막 날짜를 입력하세요(ex. 28, 29, 30, 31): '))
    if 1 <= end <= 31:
        break

while True:
    default = input('기준월 1조의 첫 번째 평일 근무 형태를 입력하세요(ex. A, B): ')
    if default == 'A' or default == 'B':
        break


# lst로 데이터프레임 형성 --> 데이터프레임을 엑셀로 변환
# 요일 붙여넣기(엑셀 기준 2번째 행을 형성)
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


# 근무자 이름 넣기(엑셀 기준 B열 형성)
for i in range(len(names)):
    table += [[names[i]] + ['' for i in range(end)]]


# 근무자 수만큼 반복
for i in range(1, len(names)+1):
    # 근무 형태(A 또는 B)
    status = default
    # 날짜 수만큼 반복
    for j in range(1, end+1):
        # 평일일 때
        if table[0][j] != '토' and table[0][j] != '일':
            # 평일 근무 형태 입력
            table[i][j] = status
        # 주말일 때
        else:
            # 다음주 평일에는 근무 형태가 바뀔 것이므로 status 바꿔줌
            # A --> B  &  B --> A
            if table[0][j] == '토':
                if status == 'B':
                    status = 'A'
                else:
                    status = 'B'


# 기준월의 첫번째 주말에 근무를 하는지 여부 입력받기
# work 변수는 1조가 이번 주말에 근무를 서는지의 여부
# work == 1 --> 1조는 이번 주말 근무
# work == 0 --> 1조는 이번 주말 휴무
work = int(input('기준월의 첫번째 주말에 1조가 근무를 하는지의 여부를 입력(근무시 1 / 근무 아닐 시 0) : '))


# brk 리스트의 값은 지지난주 주말에 휴무였던 근무자의 번호(names 리스트 상의 인덱스)
brk = [-1, -1]
prev1, prev2 = input('마지막 주말 휴무자 두 명의 이름을 띄어쓰기로 구분하여 입력하세요: ').split()
for i, name in enumerate(names):
    if brk[0] == -1 and (name == prev1 or name == prev2):
        brk[0] = i + 1
    elif name == prev1 or name == prev2:
        brk[1] = i + 1
print(brk[0], brk[1])


# save 리스트는 일요일 D를 받으면 안 되는 사람의 번호(토요일 C 또는 토요일 D인 근무자)
save = []
# 날짜 수만큼 반복
for j in range(1, end+1):
    # 근무 서는 주말
    if work and (table[0][j] == '토' or table[0][j] == '일'):
        # 지지난주 주말 휴무자 중 윗 사람 C 근무 배정
        if table[0][j] == '토':
            table[brk[0]][j] = 'C'
            save.append(brk[0])
            # 휴무자 번호 증가시키기
            brk[0] += 2
            brk[1] += 2
            if brk[0] > len(names) and brk[1] > len(names):
                brk[0] = 1
                brk[1] = 2
            elif brk[1] > len(names):
                brk[1] = 1
            elif brk[0] > len(names):
                brk[0] = brk[1] - 1
            elif brk[0] == 1 and brk[1] == len(names):
                brk[0] = 2
                brk[1] = 3
            print(brk[0], brk[1])
        # 휴무자 표시
        table[brk[0]][j] = '휴'
        table[brk[1]][j] = '휴'
        # 근무자 위 두 명 토요일 D 근무 배정
        if table[0][j] == '토':
            sat_count = 0
            for k in range(1, len(names)+1):
                if table[k][j] == '':
                    table[k][j] = 'D'
                    sat_count += 1
                    save.append(k)
                    if sat_count >= 2:
                        break
        # 나머지 두 명 일요일 D 근무 배정
        else:
            print(save)
            for k in range(1, len(names)+1):
                if table[k][j] == '' and k not in save:
                    table[k][j] = 'D'
            work = 0
    # 근무 안 서는 주말
    elif table[0][j] == '토' or table[0][j] == '일':
        if table[0][j] == '일':
            work = 1
    # 평일
    else:
        save = []


team1 = pd.DataFrame(table)
team1.columns = ['날짜'] + [i for i in range(1, end+1)]
team1.to_csv('team1.csv')


print(team1)
