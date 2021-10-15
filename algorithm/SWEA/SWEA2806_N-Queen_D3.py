T = int(input())

dr = [-1, 1, 1, -1]     # 우상, 우하, 좌하, 좌상
dc = [1, 1, -1, -1]


# 대각선 확인
def is_available(r, c):
    r_o = r
    c_o = c
    for d in range(4):
        r = r_o
        c = c_o
        while True:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if (nr, nc) in queens:
                    return False
                r, c = nr, nc
            else:
                break

    return True


def dfs(idx):
    global cnt
    if idx == N:
        cnt += 1

    for c in range(N):
        if not selected[c] and is_available(idx, c):
            queens.add((idx, c))
            selected[c] = True
            dfs(idx + 1)
            queens.discard((idx, c))
            selected[c] = False


for tc in range(1, T + 1):
    N = int(input())
    selected = [False] * N
    queens = set()
    cnt = 0
    dfs(0)
    print('#{} {}'.format(tc, cnt))