import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


dx = [-1, -1, 1, 1]     # 왼쪽 위, 오른쪽 위, 오른쪽 아래, 왼쪽 아래
dy = [-1, 1, 1, -1]

# 방향전환을 세 번만 해야 됨
# 시작점을 오른쪽 위(dir: 1) / 오른쪽 아래(dir: 2)만으로 나눠서 생각
#


def dfs(r, c, selected, direction, direction_cnt, length):
    global row, col, answer
    if direction_cnt == 4:
        if r == row and c == col:
            if answer < length:
                answer = length
        return

    if direction == 1:
        available_directions = [1, 2]
    elif direction == 2:
        available_directions = [2, 3]
    elif direction == 3:
        available_directions = [3, 0]
    else:
        available_directions = [0, 1]

    for d in available_directions:
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and cafe[nx][ny] not in selected:
                visited[nx][ny] = True
                selected.add(cafe[nx][ny])
                if d != direction:
                    dfs(nx, ny, selected, d, direction_cnt + 1, length + 1)
                else:
                    dfs(nx, ny, selected, d, direction_cnt, length + 1)
                visited[nx][ny] = False
                selected.discard(cafe[nx][ny])


for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = -1

    for row in range(N):
        for col in range(N):
            dfs(row, col, set(), 1, 0, 0)

    print('#{} {}'.format(tc, answer))