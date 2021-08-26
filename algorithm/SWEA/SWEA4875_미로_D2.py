import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def dfs(x, y):
    global N
    global result

    if maze[x][y] == 3:
        result = 1
        return

    for r in range(4):
        nx = x + dx[r]
        ny = y + dy[r]
        if (0 <= nx < N and 0 <= ny < N) and not visited[nx][ny] and maze[nx][ny] != 1:
            visited[nx][ny] = True
            dfs(nx, ny)


for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print(i, j)
            if maze[i][j] == 2:
                x, y = i, j
                break
    result = 0
    visited[x][y] = True
    dfs(x, y)
    print('#{} {}'.format(tc, result))
