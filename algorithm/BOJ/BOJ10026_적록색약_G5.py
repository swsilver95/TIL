from collections import deque

N = int(input())
data = [input() for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_rg(row, col, color):
    if color == 'B':
        target = 'B'
    else:
        target = 'RG'

    q = deque()
    visited_rg[row][col] = True
    q.append((row, col))

    while q:
        x, y = q.popleft()
        for r in range(4):
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited_rg[nx][ny] and data[nx][ny] in target:
                    q.append((nx, ny))
                    visited_rg[nx][ny] = True


def bfs_nm(row, col, color):
    target = color
    q = deque()
    visited_nm[row][col] = True
    q.append((row, col))

    while q:
        x, y = q.popleft()
        for r in range(4):
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited_nm[nx][ny] and data[nx][ny] == target:
                    q.append((nx, ny))
                    visited_nm[nx][ny] = True


visited_rg = [[False] * N for _ in range(N)]
visited_nm = [[False] * N for _ in range(N)]

cnt_rg = 0
cnt_nm = 0
for row in range(N):
    for col in range(N):
        if not visited_rg[row][col]:
            bfs_rg(row, col, data[row][col])
            cnt_rg += 1

        if not visited_nm[row][col]:
            bfs_nm(row, col, data[row][col])
            cnt_nm += 1

print(cnt_nm, cnt_rg)