from collections import deque

T = int(input())


da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]


def bfs(r, c):
    global cnt
    q = deque()
    q.append([r, c])
    visited[r][c] = True

    while q:
        a, b = q.popleft()
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if 0 <= na < N and 0 <= nb < M:
                if not visited[na][nb] and field[na][nb] == 1:
                    q.append([na, nb])
                    visited[na][nb] = True

    cnt += 1


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(M):
            if field[row][col] == 1 and not visited[row][col]:
                bfs(row, col)

    print(cnt)