N = int(input())
data = [input() for _ in range(N)]


def compress(N, r1, c1):

    if N == 1:
        return data[r1][c1]

    numtype = data[r1][c1]
    flag = True
    try:
        for r in range(r1, r1 + N):
            for c in range(c1, c1 + N):
                if data[r][c] != numtype:
                    raise AssertionError
    except AssertionError:
        flag = False

    if flag:
        return numtype
    else:
        d = N // 2
        return '(' + \
            compress(d, r1, c1) + \
            compress(d, r1, c1 + d) + \
            compress(d, r1 + d, c1) + \
            compress(d, r1 + d, c1 + d) + ')'


print(compress(N, 0, 0))

