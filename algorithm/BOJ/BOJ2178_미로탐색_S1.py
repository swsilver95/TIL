from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(input())


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    q = deque()
    q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        if r == row and c == col:
            return visited[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and maze[nr][nc] == '1':
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1


print(bfs(N - 1, M - 1))