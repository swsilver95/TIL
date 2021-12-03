from collections import deque

M, N, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# row, col, height
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]
dh = [1, -1, 0, 0, 0, 0]


def bfs():
    global t
    while q:
        height, row, col = q.popleft()
        for d in range(6):
            nh = height + dh[d]
            nr = row + dr[d]
            nc = col + dc[d]

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if not visited[nh][nr][nc] and tomato[nh][nr][nc] == 0:
                    q.append((nh, nr, nc))
                    visited[nh][nr][nc] = visited[height][row][col] + 1
                    if t < visited[nh][nr][nc]:
                        t = visited[nh][nr][nc]


q = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

for h in range(H):  # 높이
    for n in range(N):  # 행
        for m in range(M):  # 열
            if tomato[h][n][m] == 1:
                q.append((h, n, m))
                visited[h][n][m] = 1

t = 0
bfs()

flag = True
try:
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == 0 and tomato[i][j][k] != -1:
                    raise AssertionError
except AssertionError:
    flag = False

if flag:
    if t == 0:
        print(0)
    else:
        print(t - 1)
else:
    print(-1)

