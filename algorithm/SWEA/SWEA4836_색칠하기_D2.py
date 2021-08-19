import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    grid = [[0] * 10 for _ in range(10)]                    # 10X10 빈 격자 생성
    N = int(input())
    cnt = 0
    for _ in range(N):                                      # N번의 색칠 과정에 대해서
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):                         # 행 번호가 r1부터 r2
            for j in range(c1, c2 + 1):                     # 열 번호가 c1부터 c2인 지점의
                grid[i][j] += color                         # 색깔을 color로 칠해준다.(더한다.)
                if grid[i][j] == 3:                         # 칸의 색깔이 보라(3)색이면
                    cnt += 1                                # count에 1을 더한다.
    print('#{} {}'.format(tc, cnt))