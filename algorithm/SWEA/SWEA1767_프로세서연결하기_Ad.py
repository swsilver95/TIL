T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def erase(row, col, r, count):
    for _ in range(count):
        row += dr[r]
        col += dc[r]
        processor[row][col] = 0


def connect(row, col, r):
    x = row
    y = col
    line_length = 0
    while 0 <= x + dr[r] < N and 0 <= y + dc[r] < N:
        x += dr[r]
        y += dc[r]
        if processor[x][y] == 1:
            erase(row, col, r, line_length)
            break
        processor[x][y] = 1
        line_length += 1
    else:
        return line_length
    return 0


def dfs(now, last, line_length):
    global core_count, min_length
    if core_count > len(now) + (len(cores) - last):
        return

    if core_count < len(now):
        core_count = len(now)
        min_length = 9999
    if core_count == len(now) and min_length > line_length:
        min_length = line_length

    for i in range(last, len(cores)):
        row, col = cores[i][0], cores[i][1]
        for r in range(4):
            tmp = connect(row, col, r)
            if tmp == 0:
                continue
            nxt = now[:]
            nxt.append(i)
            dfs(nxt, i + 1, line_length + tmp)
            erase(row, col, r, tmp)


for tc in range(1, T + 1):
    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]

    # 코어의 위치를 탐색하여 cores에 튜플 형태로 저장
    # 벽에 붙어있는 코어는 제외한다.
    cores = []
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if processor[row][col]:
                cores.append((row, col))
    # print(cores)

    core_count = 0
    min_length = 9999
    dfs([], 0, 0)
    print('#{} {}'.format(tc, min_length))