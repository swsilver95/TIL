C, R = map(int, input().split())
K = int(input())


def turn(r):
    r += 1
    if r >= 4:
        r -= 4
    return r


def seats_number(col, row, target):
    if target == 1:
        return [1, 1]

    seats = [[0 for _ in range(col)] for _ in range(row)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    i = 1
    x = row - 1
    y = 0
    seats[x][y] = 1
    r = 0
    while i < col * row:
        nx = x + dx[r]
        ny = y + dy[r]
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            r = turn(r)
            continue
        else:
            if seats[nx][ny] != 0:
                r = turn(r)
                continue
            else:
                i += 1
                seats[nx][ny] = i
                x = nx
                y = ny
                if i == target:
                    return [y + 1, row - x]
    # print(seats)
    return 0


a = seats_number(C, R, K)
if a == 0:
    print(0)
else:
    print(*a)