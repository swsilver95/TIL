T = int(input())

dx = [0, 1] # 우, 하
dy = [1, 0]


def dfs(row, col, total):
    global answer
    if answer < total:
        return

    if row == N - 1 and col == N - 1:
        if answer > total:
            answer = total

    for r in range(2):
        nx = row + dx[r]
        ny = col + dy[r]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, total + data[nx][ny])
                visited[nx][ny] = False


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    answer = 1001
    dfs(0, 0, data[0][0])
    print('#{} {}'.format(tc, answer))
