import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def bfs(x, y):
    N = 16
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()
        for r in range(4):
            nx = a + dx[r]
            ny = b + dy[r]
            if not visited[nx][ny]:
                if maze[nx][ny] == 3:
                    return 1
                elif maze[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    x, y = 1, 1
    print('#{} {}'.format(tc, bfs(x, y)))
