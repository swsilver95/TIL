import sys
from copy import deepcopy

input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def will_submerge(x, y):
    if data[x][y] != 'X':
        return True

    cnt = 0
    for r in range(4):
        nx = x + dx[r]
        ny = y + dy[r]
        if 0 <= nx < R and 0 <= ny < C:
            if data[nx][ny] != 'X':
                cnt += 1
        else:
            cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


R, C = map(int, input().split())
data = [list(input().rstrip()) for _ in range(R)]
answer = deepcopy(data)

for row in range(R):
    for col in range(C):
        if will_submerge(row, col):
            answer[row][col] = '.'


point_row = []
point_col = []
for row in range(R):
    for col in range(C):
        if answer[row][col] == 'X':
            point_row.append(row)
            point_col.append(col)

start = [min(point_row), min(point_col)]
end = [max(point_row), max(point_col)]

for row in range(start[0], end[0] + 1):
    for col in range(start[1], end[1] + 1):
        print(answer[row][col], end='')
    print()