from copy import deepcopy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
'''
0 상
1 우
2 하
3 좌
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dr = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

cctvs = []
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctvs.append([i, j, office[i][j]])
# print(cctvs)


def dfs(p, temp, cctvs):
    global min_hide
    if p == len(cctvs):
        cnt = sum(temp, []).count(0)
        if min_hide > cnt:
            min_hide = cnt
        return

    x, y, cctv = cctvs[p]
    for directions in dr[cctv]:
        tmp = deepcopy(temp)
        for r in directions:
            nx = x + dx[r]
            ny = y + dy[r]
            while 0 <= nx < N and 0 <= ny < M:
                if tmp[nx][ny] == 6:
                    break
                elif tmp[nx][ny] == 0:
                    tmp[nx][ny] = -1
                nx += dx[r]
                ny += dy[r]
        dfs(p + 1, tmp, cctvs)


min_hide = 65
dfs(0, office, cctvs)
print(min_hide)