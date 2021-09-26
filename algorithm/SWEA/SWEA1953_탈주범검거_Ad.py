from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

"""
1: 상하좌우 [0, 1, 2, 3]
2: 상하 [0, 1]
3: 좌우 [2, 3]
4: 상우 [0, 3]
5: 하우 [1, 3]
6: 하좌 [1, 2]
7: 상좌 [0, 2]
"""
case = {
    0: [],
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}


def reverse(r):
    if r == 0:
        return 1
    if r == 1:
        return 0
    if r == 2:
        return 3
    if r == 3:
        return 2


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        pipe = case.get(data[x][y])
        # print(data[x][y])
        # print(pipe)
        for r in pipe:
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if reverse(r) in case.get(data[nx][ny]):
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1

    return visited


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())   # N: 지도 세로 / M: 지도 가로 / R: 맨홀 row / C: 맨홀 col / L: 경과시간
    data = [list(map(int, input().split())) for _ in range(N)]

    V = bfs(R, C)
    cnt = 0
    for row in range(N):
        for col in range(M):
            if V[row][col] != 0 and V[row][col] <= L:
                cnt += 1

    print('#{} {}'.format(tc, cnt))