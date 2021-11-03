import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def can_move(row, col):
    available = []
    for d in range(4):
        r = row
        c = col
        flag = False
        endflag = False
        while True:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if flag:
                    if not endflag:
                        available.append((nr, nc))
                        if board[nr][nc] == 1:
                            endflag = True
                    if endflag:
                        break
                else:
                    if board[nr][nc] == 1:
                        flag = True
                r, c = nr, nc
            else:
                break
    return available


def dfs(row, col, move_cnt):
    global answer
    if move_cnt == 3:
        return

    for next_row, next_col in can_move(row, col):
        visited[next_row][next_col] = True
        temp = board[next_row][next_col]
        board[next_row][next_col] = 2
        board[row][col] = 0
        dfs(next_row, next_col, move_cnt + 1)
        board[next_row][next_col] = temp
        board[row][col] = 2


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    start = (0, 0)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)

    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    answer = 0
    dfs(start[0], start[1], 0)

    for i in range(N):
        for j in range(N):
            if visited[i][j] and board[i][j] == 1:
                answer += 1

    print('#{} {}'.format(tc, answer))

