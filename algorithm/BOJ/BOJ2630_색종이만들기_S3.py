N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0


def divide(N, r1, c1, r2, c2):
    global blue, white

    cnt_blue = 0
    cnt_white = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if paper[r][c]:
                cnt_blue += 1
            else:
                cnt_white += 1

    if cnt_blue == N ** 2:
        blue += 1
        return

    elif cnt_white == N ** 2:
        white += 1
        return

    else:
        mid_r = (r1 + r2) // 2
        mid_c = (c1 + c2) // 2
        divide(N // 2, r1, c1, mid_r, mid_c)            # 좌상
        divide(N // 2, r1, mid_c + 1, mid_r, c2)        # 우상
        divide(N // 2, mid_r + 1, c1, r2, mid_c)        # 좌하
        divide(N // 2, mid_r + 1, mid_c + 1, r2, c2)    # 우하


divide(N, 0, 0, N - 1, N - 1)
print(white)
print(blue)
