from collections import deque

board = [[0] * 6 for _ in range(6)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity():
    global board
    tp_board = list(zip(*board))
    tp_board = [list(index[:]) for index in tp_board]
    for row in range(6):
        for col in range(6):
            if tp_board[row][col] == 0:
                tp_board[row].pop(col)
                tp_board[row].insert(0, 0)

    board = list(zip(*tp_board))
    board = [list(index[:]) for index in board]


def erase(s_row, s_col, color):
    q = deque()
    q.append((s_row, s_col))
    visited = [[0] * 6 for _ in range(6)]
    visited[s_row][s_col] = 1
    board[s_row][s_col] = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 6 and 0 <= nc < 6:
                if not visited[nr][nc] and board[nr][nc] == color:
                    q.append((nr, nc))
                    board[nr][nc] = 0


def bfs(s_row, s_col, color):
    q = deque()
    q.append((s_row, s_col))
    visited = [[0] * 6 for _ in range(6)]
    visited[s_row][s_col] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 6 and 0 <= nc < 6:
                if not visited[nr][nc] and board[nr][nc] == color:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    # print(visited)
    max_val = max(sum(visited, []))
    if max_val >= 3:
        return True
    else:
        return False


def put(idx, color):
    target_row = 0
    for row in range(6):
        if board[row][idx]:
            target_row = row - 1
            break
    else:
        target_row = 5

    board[target_row][idx] = color
    return (target_row, idx)


def solution(macaron):
    for m in macaron:
        idx, color = m
        row, col = put(idx - 1, color)
        # 연쇄반응을 잘 고려하지 못했음
        if bfs(row, col, color):
            erase(row, col, color)
            gravity()

        k = 0
        while k <= 36:
            for ii in range(6):
                for jj in range(6):
                    k += 1
                    color = board[ii][jj]
                    if color != 0:
                        if bfs(ii, jj, color):
                            erase(ii, jj, color)
                            gravity()
                            k = 0
    return board


macaron = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]
print(solution(macaron))