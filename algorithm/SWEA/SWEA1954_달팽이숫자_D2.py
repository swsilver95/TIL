T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(r):
    r += 1
    if r >= 4:
        r -= 4
    return r

for idx in range(T):
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    r = 0
    x = 0
    y = 0
    tmp = 1
    snail[x][y] = 1
    # print(snail)
    while tmp < n * n:
        x += dx[r]
        y += dy[r]
        # print(x, y)
        if x < 0 or y < 0 or x >= n or y >= n:
            x -= dx[r]
            y -= dy[r]
            r = turn(r)
            continue

        if snail[x][y] != 0:
            x -= dx[r]
            y -= dy[r]
            r = turn(r)
            continue
        
        tmp += 1
        # print(f'--{tmp}')
        snail[x][y] = tmp
    
    print(f'#{idx + 1}')
    for i in range(n):
        print(' '.join(map(str, snail[i])))