import sys

N, r, c = map(int, input().split())

now = 0


def fill(r1, c1, r2, c2):
    global now

    if r1 == r2 and c1 == c2:
        if r == r1 and c == c1:
            print(now)
            sys.exit(0)
        else:
            now += 1
        return

    else:
        if not (r1 <= r <= r2) and not (c1 <= c <= c2):
            now += (r2 - r1 + 1) ** 2
            return

        mid_r = (r1 + r2) // 2
        mid_c = (c1 + c2) // 2
        fill(r1, c1, mid_r, mid_c)
        fill(r1, mid_c + 1, mid_r, c2)
        fill(mid_r + 1, c1, r2, mid_c)
        fill(mid_r + 1, mid_c + 1, r2, c2)


fill(0, 0, 2 ** N - 1, 2 ** N - 1)
