import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())                    # 0. N은 열 수, M은 행 수
    flag = [list(map(str, input())) for _ in range(N)]  # 0. 깃발 데이터를 str 형태로 받아옴
    idx_list = list(combinations(range(1, N), 2))       # 1. N을 3분할하기 위해서 1부터 N-1까지 두 수를 선택하는 경우의 수
    min_cnt = 2501                                      # 2. 최소 변경 횟수 변수를 문제 조건에 따라 초기화
    # print(idx_list)
    for idx in idx_list:                # 3. 경우의 수에서 하나를 뗴어 와서
        a = idx[0]                      # 3-1. a번째 줄까지 흰색
        b = idx[1]                      # 3-2. a+1번째 줄부터 b번째 줄까지 파란색
        c = N                           # 3-3. b+1번째 줄부터 c번째 줄까지 빨간색을 칠하면 된다.

        cnt = 0                         # 4. 칠하는 과정 시작
        for i in range(a):              # 4-1. a번째 줄까지 흰색으로 칠해야 되는 횟수
            for j in range(M):
                if flag[i][j] != 'W':
                    cnt += 1

        for i in range(a, b):           # 4-2. b번째 줄까지 파란색으로 칠해야 되는 횟수
            for j in range(M):
                if flag[i][j] != 'B':
                    cnt += 1

        for i in range(b, c):           # 4-3. c번째 줄까지 빨간색으로 칠해야 되는 횟수
            for j in range(M):
                if flag[i][j] != 'R':
                    cnt += 1

        if min_cnt > cnt:               # 5. 지금까지 나온 최소 횟수와 비교해서
            min_cnt = cnt               # 5-1. 최소 색칠 횟수를 업데이트

    print('#{} {}'.format(tc, min_cnt))
