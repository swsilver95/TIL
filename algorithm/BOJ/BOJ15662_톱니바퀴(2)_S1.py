T = int(input())
gears = []
for _ in range(T):
    gears.append(list(map(int, input())))


def rotate(n, r):
    if r == 1:
        a = gears[n - 1].pop()
        gears[n - 1].insert(0, a)
    else:
        a = gears[n - 1].pop(0)
        gears[n - 1].append(a)


def run_left(n, r):
    if n <= 1:
        return
    else:
        if gears[n - 1][-2] != gears[n - 2][2]:
            if n - 2 == 0:
                rotate(n - 1, -r)
            else:
                if gears[n - 2][-2] != gears[n - 3][2]:
                    run_left(n - 1, -r)
                rotate(n - 1, -r)
        else:
            return


def run_right(n, r):
    if n >= T:
        return
    else:
        if gears[n][-2] != gears[n - 1][2]:
            if n + 1 == T:
                rotate(n + 1, -r)
            else:
                if gears[n + 1][-2] != gears[n][2]:
                    run_right(n + 1, -r)
                rotate(n + 1, -r)
        else:
            return


K = int(input())
for _ in range(K):
    n, r = map(int, input().split())
    run_left(n, r)
    run_right(n, r)
    rotate(n, r)

cnt = 0
for gear in gears:
    if gear[0] == 1:
        cnt += 1

print(cnt)
