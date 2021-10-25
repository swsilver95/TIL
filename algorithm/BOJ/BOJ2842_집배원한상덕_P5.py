from collections import deque

N = int(input())
village = [list(map(str, input())) for _ in range(N)]
heights = [list(map(int, input().split())) for _ in range(N)]
one_heights = []
for h in heights:
    one_heights.extend(h)


dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

houses = set()
start = 0
end = 0

for i in range(N):
    for j in range(N):
        if village[i][j] == 'P':
           start, end = i, j
        elif village[i][j] == 'K':
            houses.add((i, j))

answer = 1000001
one_heights.sort()
left = 0
right = 0
while left <= right:
    visited = [[False] * N for _ in range(N)]
    q = deque()
    if one_heights[left] <= heights[start][end] <= one_heights[right]:
        visited[start][end] = True
        q.append((start, end))

    cnt = 0
    while q:
        r, c = q.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if one_heights[left] <= heights[nr][nc] <= one_heights[right]:
                    if (nr, nc) in houses:
                        cnt += 1
                    visited[nr][nc] = True
                    q.append((nr, nc))

    if cnt == len(houses):
        answer = min(answer, one_heights[right] - one_heights[left])
        left += 1
    elif right + 1 < len(one_heights):
        right += 1
    else:
        break

print(answer)

