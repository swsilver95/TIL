import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()
        for r in range(4):
            nx = a + dx[r]
            ny = b + dy[r]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if maze[nx][ny] == 3:
                        visited[nx][ny] = visited[a][b] + 1
                        return visited[nx][ny] - 2
                    elif maze[nx][ny] != 1:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[a][b] + 1
    return 0


for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
                break
    print('#{} {}'.format(tc, bfs(x, y)))