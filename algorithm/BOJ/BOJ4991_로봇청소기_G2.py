import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]


def bfs(x, y):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        a, b = q.popleft()
        for r in range(4):
            na = a + da[r]
            nb = b + db[r]
            if 0 <= na < h and 0 <= nb < w:
                if not visited[na][nb] and room[na][nb] != 'x':
                    q.append([na, nb])
                    visited[na][nb] = visited[a][b] + 1

    return visited


def solution():
    dusts = []
    i = 1
    for height in range(h):
        for width in range(w):
            if room[height][width] == '*':
                dusts.append([height, width, i])
                i += 1
            elif room[height][width] == 'o':
                start = [height, width]

    start_x, start_y = start
    all_visited = [bfs(start_x, start_y)]
    for dust in dusts:
        dust_x, dust_y, idx = dust
        if all_visited[0][dust_x][dust_y] == 0:
            return -1

    for dust in dusts:
        p1, p2, num = dust
        all_visited.append(bfs(p1, p2))

    answer = 9999999999
    cases = list(permutations(dusts, len(dusts)))

    for case in cases:
        tmp = 0
        for i in range(len(case)):
            if i == 0:
                x1, y1, idx1 = case[0]
                tmp += all_visited[0][x1][y1] - 1
            else:
                x1, y1, idx1 = case[i - 1]
                x2, y2, idx2 = case[i]
                tmp += all_visited[idx1][x2][y2] - 1
        if answer > tmp:
            answer = tmp

    return answer


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    room = [list(input()) for _ in range(h)]
    print(solution())