T = int(input())


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def proliferate():
    now = {}
    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] != 0:
                # 비활성 상태이면 비활성 수치를 1 감소시킴
                if lifepower[row][col] > 0:
                    lifepower[row][col] -= 1
                # 비활성 수치가 0 이하라면 -> 증식 시작 가능
                else:
                    # 수명이 다한 경우에는 그냥 패스( ex. 생명력 수치가 3인데 활성수치가 -4이면 더이상 증식 불가능)
                    if lifepower[row][col] <= -grid[row][col]:
                        continue
                    # 수명이 다하지 않았을 때는 상하좌우로 증식
                    for d in range(4):
                        nr = row + dr[d]
                        nc = col + dc[d]
                        # 이동 방향의 셀이 빈 셀이면 now에 추가
                        if grid[nr][nc] == 0 and (nr, nc) not in now:
                            now[(nr, nc)] = grid[row][col]
                        # 이번 증식에서 동일한 위치로 증식하려고 하는 경우
                        elif (nr, nc) in now:
                            # 증식된 위치의 생명력이 현재 세포보다 작으면 덮어씌움
                            if now.get((nr, nc)) < grid[row][col]:
                                now[(nr, nc)] = grid[row][col]
                    # 증식했으면 활성수치를 1 감소시킴 (세포의 파워가 3이라고 하면 -1, -2, -3 총 세 번 증식이 가능)
                    lifepower[row][col] -= 1

    for key, life in now.items():
        row1, col1 = key
        grid[row1][col1] = life
        lifepower[row1][col1] = life


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(N)]
    SIZE = max(N, M) + K * 2
    grid = [[0] * SIZE for _ in range(SIZE)]
    lifepower = [[0] * SIZE for _ in range(SIZE)]

    for i in range(N):
        for j in range(M):
            grid[SIZE//2 - N + i][SIZE//2 - M + j] = cells[i][j]
            lifepower[SIZE//2 - N + i][SIZE//2 - M + j] = cells[i][j]

    for time in range(K):
        proliferate()

    answer = 0
    for r in range(SIZE):
        for c in range(SIZE):
            # 세포가 있으면서
            if grid[r][c] != 0:
                # 해당 세포가 죽지 않았으면
                if lifepower[r][c] > -grid[r][c]:
                    answer += 1

    print('#{} {}'.format(tc, answer))
