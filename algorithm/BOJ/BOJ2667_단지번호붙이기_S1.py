from collections import deque

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


visited = [[0] * N for _ in range(N)]
houses = []


def bfs(row, col):
    q = deque()
    q.append((row, col))
    tmp = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if (not visited[nr][nc]) and board[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    tmp += 1

    houses.append(tmp + 1)


cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j)
            cnt += 1

print(cnt)
houses.sort()
for house in houses:
    print(house)

