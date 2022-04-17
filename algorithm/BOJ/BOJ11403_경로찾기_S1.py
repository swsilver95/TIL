from collections import deque

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

for start in range(N):
    for end in range(N):
        if adj[start][end]:
            graph[start].append(end)


def bfs(s, e):
    visited = [False] * N
    visited[s] = True
    q = deque()
    q.append(s)

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if next_node == e:
                return True

            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return False


for i in range(N):
    for j in range(N):
        if bfs(i, j):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
