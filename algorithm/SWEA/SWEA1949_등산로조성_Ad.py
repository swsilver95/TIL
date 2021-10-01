T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, dig):
    global answer

    for r in range(4):
        nx = x + dx[r]
        ny = y + dy[r]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                if data[x][y] > data[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    dfs(nx, ny, dig)
                    visited[nx][ny] = 0

                elif dig:
                    if data[x][y] > data[nx][ny] - K:
                        temp = data[nx][ny]
                        data[nx][ny] = data[x][y] - 1
                        visited[nx][ny] = visited[x][y] + 1
                        dfs(nx, ny, False)
                        visited[nx][ny] = 0
                        data[nx][ny] = temp

    if answer < visited[x][y]:
        answer = visited[x][y]


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_val = max(sum(data, []))
    peaks = []
    for row in range(N):
        for col in range(N):
            if data[row][col] == max_val:
                peaks.append([row, col])

    answer = 0
    for peak in peaks:
        x, y = peak
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[x][y] = 1
        dfs(x, y, True)

    print('#{} {}'.format(tc, answer))