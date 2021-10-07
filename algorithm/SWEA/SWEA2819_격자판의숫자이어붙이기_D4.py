T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, cnt, num):
    if cnt == 7:
        answer.add(num)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, cnt + 1, num + data[nr][nc])


for tc in range(1, T + 1):
    data = [list(map(str, input().split())) for _ in range(4)]
    answer = set()

    for row in range(4):
        for col in range(4):
            dfs(row, col, 0, '')

    print('#{} {}'.format(tc, len(answer)))