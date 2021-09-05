from collections import deque

N = int(input())
fishes = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 다음 먹을 물고기의 위치를 찾는 함수
def find_target(shark_size, shark_position):
    edible_fishes = []  # 먹을 수 있는 물고기의 좌표
    # 어떤 물고기의 크기가 상어의 크기보다 작으면, 해당 물고기의 좌표와 물고기까지의 거리를 edible_fishes에 저장
    dist = check_distance(shark_position)
    for i in range(N):
        for j in range(N):
            if fishes[i][j] != 0 and fishes[i][j] < shark_size and dist[i][j]:
                edible_fishes.append([i, j, dist[i][j] - 1])

    # 만약 공간에 먹을 수 있는 물고기가 없으면 빈 리스트 반환
    if len(edible_fishes) == 0:
        return []
    # 먹을 수 있는 물고기가 한 마리 뿐이라면, 해당 물고기의 좌표를 반환
    elif len(edible_fishes) == 1:
        return edible_fishes[0]
    # 먹을 수 있는 물고기가 한 마리 이상이라면, 거리를 기준으로 정렬하여 가장 앞에 있는 물고기의 좌표를 반환
    else:
        new = sorted(edible_fishes, key=lambda x: x[2])
        return new[0]


# BFS로 거리를 찾아 visited 형태로 반환하는 함수
def check_distance(shark_position):
    q = deque()
    q.append(shark_position)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[shark_position[0]][shark_position[1]] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동한 방향이 정상적인 방향이면서, 해당 위치에 물고기가 없거나 크기가 상어보다 작거나 같은 물고기가 있을 때,
            if 0 <= nx < N and 0 <= ny < N and fishes[nx][ny] <= shark_size:
                # 이미 방문한 위치가 아니라면, 해당 위치를 방문처리하고 큐에 추가
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

    return visited


# 입력값에 대해 상어의 위치를 [i, j] 형태로 반환해주는 과정
for i in range(N):
    for j in range(N):
        if fishes[i][j] == 9:
            shark_position = [i, j]
            break

shark_size = 2  # 상어의 크기를 2로 초기화, 잡아먹으러 갈 물고기를 target_position으로 저장
target_position = find_target(shark_size, shark_position)
fishes[shark_position[0]][shark_position[1]] = 0    # 처음 상어가 있던 위치를 0으로 초기화
time = 0        # 상어가 먹으러 돌아다닌 총 시간
eat_count = 0   # 현재 상어 크기에서 먹어치운 물고기의 수

# 잡아먹으러 갈 물고기가 최소 한마리라도 있는 동안에 돌아갈 루프
while target_position:
    if target_position:             # tmp는 [x, y, t] 형태로 반환됨
        time += target_position[2]
        shark_position = [target_position[0], target_position[1]]
        fishes[target_position[0]][target_position[1]] = 0
        eat_count += 1
        # 상어가 자신의 크기와 같은 수의 물고기를 먹어치웠을 경우
        if shark_size == eat_count:
            eat_count = 0       # 먹은 수를 초기화하고
            shark_size += 1     # 상어의 크기를 1 늘려줌
            
        # 다시 다음 먹으러 갈 물고기의 위치를 찾아줌
        target_position = find_target(shark_size, shark_position)
    # 만약 잡아먹으러 갈 물고기가 있음에도 불구하고 해당 위치에 막혀서 도착할 수 없는 경우,
    else:
        target_position = []        # 루프문을 끝내기 위해 target_position을 빈 리스트로 변경

print(time)