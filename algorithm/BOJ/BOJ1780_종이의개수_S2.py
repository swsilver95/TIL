N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

x = y = z = 0


def divide(size, index):
    global x, y, z
    r1, c1 = index
    if size == 1:
        if paper[r1][c1] == -1:
            x += 1
        elif paper[r1][c1] == 0:
            y += 1
        else:
            z += 1
        return

    # 같은 숫자 판별 로직
    tmp = paper[r1][c1]
    flag = True
    try:
        for r in range(r1, r1 + size):
            for c in range(c1, c1 + size):
                if paper[r][c] != tmp:
                    raise AssertionError

    except AssertionError:
        flag = False

    if flag:
        if tmp == -1:
            x += 1
        elif tmp == 0:
            y += 1
        else:
            z += 1
        return

    s = size // 3

    p00 = (r1, c1)
    p01 = (r1, c1 + s)
    p02 = (r1, c1 + s + s)
    p10 = (r1 + s, c1)
    p11 = (r1 + s, c1 + s)
    p12 = (r1 + s, c1 + s + s)
    p20 = (r1 + s + s, c1)
    p21 = (r1 + s + s, c1 + s)
    p22 = (r1 + s + s, c1 + s + s)

    divide(s, p00)
    divide(s, p01)
    divide(s, p02)
    divide(s, p10)
    divide(s, p11)
    divide(s, p12)
    divide(s, p20)
    divide(s, p21)
    divide(s, p22)


divide(N, (0, 0))

print(x)
print(y)
print(z)
