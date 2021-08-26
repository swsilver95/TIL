import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())


def bfs(v, end):
    visited = [0] * (V + 1)
    visited[v] = 1
    q = deque()
    q.append(v)

    while q:
        p = q.popleft()
        for node in Graph[p]:
            if not visited[node]:
                q.append(node)
                visited[node] = visited[p] + 1
                if node == end:
                    return visited[node] - 1
    return 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    Graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        n, m = map(int, input().split())
        Graph[n].append(m)                          # 방향이 없으므로 양방향 추가
        Graph[m].append(n)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, bfs(S, G)))