from collections import deque
from itertools import combinations

N = int(input())
populations = [0] + list(map(int, input().split()))
graph = [set() for _ in range(N + 1)]


# start 지점에서 include 배열의 모든 지점이 연결되어 있는지 확인하는 bfs 함수
# include의 노드들과는 같은 그룹에 있다는 것을 의미함
def bfs(start, include):
    q = deque()
    q.append(start)
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        p = q.popleft()
        for next_p in graph[p]:
            # 다음 위치를 방문하지 않았으면서, 다음 위치가 같은 그룹 내의 노드인 경우
            if not visited[next_p] and next_p in include:
                q.append(next_p)
                visited[next_p] = True

    # include(같은 그룹)의 노드들을 모두 방문했는지 파악
    # 하나라도 방문하지 않았으면 연결되지 않았다는 뜻
    for node in include:
        if not visited[node]:
            return False
    return True


for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    # 양방향 그래프이므로, 양쪽의 데이터에 모두 기입
    for j in range(1, n + 1):
        graph[i].add(tmp[j])
        graph[tmp[j]].add(i)

# combinations를 사용하기 위한 배열, 인덱스를 뽑을 것
idx_list = list(range(1, N + 1))

# group1의 가능한 모든 경우의 수를 담을 배열
cases = []

# 출력할 정답, 최소치를 찾아야 하므로 임의의 큰 수로 초기화
answer = 9999999

# 두 그룹만 보면 되므로, 전체 길이(N)를 2로 나눈 몫까지만 그룹 1 조합을 뽑아내면 된다.
# 그룹 2는 그룹 1이 아닌 나머지이므로 자동으로 결정된다.
for k in range(1, N // 2 + 1):
    cases.extend(list(combinations(idx_list, k)))

# 두 그룹을 나누는 부분
for case in cases:
    # 혹시 모를 에러상황을 대비해 group1(g1)을 list로 구조 통일
    g1 = list(case)

    # g1에 속하지 않은 나머지 모두가 g2
    g2 = []
    for a in range(1, N + 1):
        if a not in g1:
            g2.append(a)

    # g1에 속한 모든 노드가 연결되어 있고, g2에 속한 모든 노드 역시 연결되어 있다면, 거리의 차이를 계산
    if bfs(g1[0], g1) and bfs(g2[0], g2):
        pop1 = 0
        pop2 = 0
        for city in g1:
            pop1 += populations[city]
        for city in g2:
            pop2 += populations[city]
        
        diff = abs(pop1 - pop2)
        # 최소 거리 갱신
        if answer > diff:
            answer = diff

# 그룹으로 나누는게 불가능하다면 -1 출력
if answer == 9999999:
    print(-1)
else:
    print(answer)