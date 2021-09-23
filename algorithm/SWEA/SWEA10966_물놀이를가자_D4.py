from collections import deque

T = int(input())

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    q = deque()

    for row in range(N):
        for col in range(M):
            if data[row][col] == 'W':
                q.append((row, col))
                visited[row][col] = 0

    while q:
        a, b = q.popleft()
        for r in range(4):
            na = a + da[r]
            nb = b + db[r]
            if 0 <= na < N and 0 <= nb < M:
                if visited[na][nb] == -1:
                    q.append((na, nb))
                    visited[na][nb] = visited[a][b] + 1

    answer = 0
    for i in range(N):
        for j in range(M):
            answer += visited[i][j]

    # print(data)
    # print(visited)
    print('#{} {}'.format(tc, answer))
