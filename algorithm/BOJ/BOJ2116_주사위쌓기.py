import sys
input = sys.stdin.readline


n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

'''
밑면 관계
0번 - 5번 : 1, 2, 3, 4
1번 - 3번 : 0, 2, 4, 5
2번 - 4번 : 0, 1, 3, 5
'''

def side_max(numbers, idx):                         # 주사위와 밑면 인덱스를 넣으면
    d_zerofive = [1, 2, 3, 4]                       # 옆면 중에서 가장 큰 숫자를 반환하는 함수
    d_onethree = [0, 2, 4, 5]
    d_twofour = [0, 1, 3, 5]
    if idx == 0 or idx == 5:
        max_sidenum = 0
        for i in d_zerofive:
            if max_sidenum < numbers[i]:
                max_sidenum = numbers[i]
    elif idx == 1 or idx == 3:
        max_sidenum = 0
        for i in d_onethree:
            if max_sidenum < numbers[i]:
                max_sidenum = numbers[i]
    else:
        max_sidenum = 0
        for i in d_twofour:
            if max_sidenum < numbers[i]:
                max_sidenum = numbers[i]
    return max_sidenum

def find_opposite(n):                               # 입력된 인덱스의 반댓면 인덱스를 반환하는 함수
    dx = [0, 1, 2, 3, 4, 5]                         # 밑면 인덱스를 넣으면 윗면 인덱스를 반환함
    dy = [5, 3, 4, 1, 2, 0]
    for i in range(6):
        if n == dx[i]:
            return dy[i]

total = 0
for i in range(1, 7):                               # 첫번째 주사위 밑면을 모두 고려
    tmp = 0                                         # (1/6) 케이스의 옆면 총합을 계산
    idx = dices[0].index(i)                         # 첫 번째 주사위 윗면의 인덱스
    j = 0
    while j <= n - 1:                               # dices의 행을 순회할 행 인덱스 j를 지정해서 while문 반복
        tmp += side_max(dices[j], idx)              # 옆면 중에서 최대값을 합하고
        # print(tmp, 'tmp')
        j += 1                                      # 다음 행으로 이동
        if j >= n:                                  # 만약 다음 행이 존재하지 않는다면 break
            break
        # print(j, 'j')
        tmp_idx = dices[j].index(dices[j - 1][idx]) # 다음 주사위의 밑면의 인덱스를 찾아 저장
        # print(tmp_idx, 'tmp_idx')
        idx = find_opposite(tmp_idx)                # find_opposite 함수를 통해 윗면의 인덱스를 찾아 반환
    total = max(total, tmp)                         # 전체 경우의 최대값을 변경하면서 다시 for문으로 돌아감
    # print(total, '___')
print(total)