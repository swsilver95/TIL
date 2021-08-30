T = int(input().rstrip())
# from pandas import DataFrame


def check_dir(x, y, color):
    if color == 1:
        other = 2
    else:
        other = 1

    possible_directions = []
    for r in range(8):
        nx = x + dx[r]
        ny = y + dy[r]
        if nx <= 0 or ny <= 0 or nx > N or ny > N:
            continue
        else:
            if board[nx][ny] == other:
                while 0 < nx <= N and 0 < ny <= N:
                    if board[nx][ny] == 0:
                        break

                    if board[nx][ny] == color:
                        possible_directions.append(r)
                        break
                    nx += dx[r]
                    ny += dy[r]

    return possible_directions


def put(x, y, color, possible_directions):
    # print(possible_directions, 'pd')
    board[x][y] = color

    for r in possible_directions:
        nx = x + dx[r]
        ny = y + dy[r]

        while board[nx][ny] != color:
            board[nx][ny] = color
            nx += dx[r]
            ny += dy[r]


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하좌우/ 대각 왼쪽 위부터 시계방향
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    board = [[0] * (N + 1) for _ in range(N + 1)]   # 오셀로 판, 인덱스 맞추기 위해 N + 1
    '''
    흑돌 1
    백돌 2
    '''
    setting = [[2, 1],
               [1, 2]]
    for i in range(2):
        for j in range(2):
            board[N//2 + i][N//2 + j] = setting[i][j]

    # print(DataFrame(board))

    for _ in range(M):
        y, x, color = map(int, input().split())
        pos = check_dir(x, y, color)
        if pos:
            put(x, y, color, pos)
        # print(y, x)
        # print(DataFrame(board))

    black = sum(board, []).count(1)
    white = sum(board, []).count(2)

    print('#{} {} {}'.format(tc, black, white))




