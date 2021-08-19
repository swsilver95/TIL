import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(S, G):
    global V
    stk = [S]
    visited = [False for _ in range(V + 1)]

    while stk:
        p = stk.pop()
        visited[p] = True
        if visited[G]:
            return 1

        for node in graph[p]:                           # 연결된 경로 중에서
            if not visited[node]:                       # 방문하지 않은 경로가 있다면
                stk.append(node)                        # 해당 경로로 이동(stack에 push)

    return 0

for tc in range(1, T + 1):
    V, E = map(int, input().split())                    # V개의 노드, E개의 경로
    graph = [[] for _ in range(V + 1)]                  # 그래프 형태로 노드 정보를 저장
    for _ in range(E):
        n, m = map(int, input().split())
        graph[n].append(m)                              # 단방향 노드

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S, G)))