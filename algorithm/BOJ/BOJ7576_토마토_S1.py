from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(q):
    length = 0
    while q:
        x, y = q.popleft()
        if visited[x][y] > length:
            length = visited[x][y]

        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return length


q = deque()
visited = [[0] * M for _ in range(N)]

for row in range(N):
    for col in range(M):
        if tomato[row][col] == 1:
            q.append((row, col))
            visited[row][col] = 1

        elif tomato[row][col] == -1:
            visited[row][col] = -1


def solve():
    day = bfs(q)
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and tomato[i][j] == 0:
                print(-1)
                return

    print(day - 1)


solve()