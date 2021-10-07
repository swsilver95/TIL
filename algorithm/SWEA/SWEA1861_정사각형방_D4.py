T = int(input())


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, length):
    global answer
    if answer < length:
        answer = length

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if room[nr][nc] == room[r][c] + 1:
                dfs(nr, nc, length + 1)


for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    tmp = []
    for row in range(N):
        for col in range(N):
            answer = 0
            dfs(row, col, 1)
            tmp.append((room[row][col], answer))

    tmp.sort(key=lambda x: (-x[1], x[0]))
    print('#{} {} {}'.format(tc, tmp[0][0], tmp[0][1]))
