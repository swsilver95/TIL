N = int(input())
K = int(input())


def dfs(node):

    for p in graph[node]:
        if not visited[p]:
            visited[p] = True
            dfs(p)


graph = [[] for _ in range(N + 1)]
for _ in range(K):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [False] * (N + 1)
visited[1] = True
dfs(1)
answer = visited.count(True) - 1
print(answer)