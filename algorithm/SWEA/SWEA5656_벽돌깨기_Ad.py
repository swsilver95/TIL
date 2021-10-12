# 14:20
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_top(idx, new_board):
    for row in range(H):
        # 선택한 인덱스의 최상단 블록을 선택하고
        if new_board[row][idx] != 0:
            # 파괴된 블록에 추가한 다음
            destroyed_blocks.add((row, idx))
            visited.add((row, idx))
            # 블록 파괴 함수 호출
            return destroy((row, idx, new_board[row][idx]), new_board)


def destroy(information, new_board):
    r, c, power = information

    # 상하좌우 방향으로
    for d in range(4):
        nr = r
        nc = c
        i = 0
        # 파워 - 1만큼 모든 블록을 불러와 파괴함수 호출
        # 파괴된 블록 리스트에도 추가
        while i < power - 1:
            i += 1
            nr += dr[d]
            nc += dc[d]
            if 0 <= nr < H and 0 <= nc < W:
                if (nr, nc) not in visited and new_board[nr][nc]:
                    destroyed_blocks.add((nr, nc))
                    visited.add((nr, nc))
                    destroy((nr, nc, new_board[nr][nc]), new_board)
            else:
                break


def cleaning(new_board, cnt):
    if cnt < len(destroyed_blocks):
        cnt = len(destroyed_blocks)

    for row in range(H):
        for col in range(W):
            if (row, col) in destroyed_blocks:
                new_board[row][col] = 0

    destroyed_blocks.clear()
    visited.clear()

    # 전치행렬로 낙하처리
    tp_board = list(zip(*new_board))
    tp_board = [list(index[:]) for index in tp_board]
    # print(tp_board)
    for row in range(W):
        col = 0
        while col < H:
            if tp_board[row][col] == 0:
                tp_board[row].pop(col)
                tp_board[row] = [0] + tp_board[row]
            col += 1

    new_board = list(zip(*tp_board))
    new_board = [list(index[:]) for index in new_board]
    return (cnt, new_board)


def dfs(sel, destroyed, new_board):
    global answer, N
    if sel == N:
        if answer < destroyed:
            answer = destroyed
        return

    for j in range(W):
        cnt = 0
        find_top(j, new_board)
        copy_board = [index[:] for index in new_board]
        temp = cleaning(new_board, cnt)
        cnt = temp[0]
        new_board = temp[1]
        dfs(sel + 1, destroyed + cnt, new_board)
        new_board = copy_board


for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    destroyed_blocks = set()
    visited = set()
    answer = 0
    new_board = [index[:] for index in board]
    dfs(0, 0, new_board)
    all_cnt = 0

    for row in range(H):
        for col in range(W):
            if board[row][col]:
                all_cnt += 1

    print('#{} {}'.format(tc, all_cnt - answer))
