def solution(n):
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    def turn(r):
        r += 1
        if r >= 3:
            r -= 3
        return r

    snail = [[0] * n for _ in range(n)]
    x = 0
    y = 0
    r = 0
    snail[0][0] = 1
    p = 1
    while p <= n*(n+1)/2 - 1:
        nx = x + dx[r]
        ny = y + dy[r]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            r = turn(r)
            continue

        if snail[nx][ny] != 0:
            r = turn(r)
            continue

        p += 1    
        snail[nx][ny] = p
        x = nx
        y = ny
    snail_list = []
    for i in snail:
        for j in i:
            if j != 0:
                snail_list.append(j)
    return snail_list

# n = int(input())
# print(solution(n))