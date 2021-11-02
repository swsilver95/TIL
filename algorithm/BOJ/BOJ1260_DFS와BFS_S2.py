from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]


def dfs(node):
    print(node, end=' ')

    for p in graph[node]:
        if not visited[p]:
            visited[p] = True
            dfs(p)


def bfs(node):
    q = deque()
    q.append(node)
    vis = [False] * (N + 1)
    vis[node] = True

    while q:
        p = q.popleft()
        print(p, end=' ')
        for next_p in graph[p]:
            if not vis[next_p]:
                vis[next_p] = True
                q.append(next_p)


for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for g in graph:
    g.sort()

visited = [False] * (N + 1)
visited[V] = True
dfs(V)
print()
bfs(V)
