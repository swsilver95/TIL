import sys

sys.stdin = open('input.txt')


def dfs(graph):
    stk = [0]
    visited = [False for _ in range(100)]
    while stk:
        p = stk.pop()
        visited[p] = True
        if p == 99:
            return 1

        for node in graph[p]:
            if not visited[node]:
                stk.append(node)

    return 0


for tc in range(1, 11):
    tc, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    for i in range(0, n * 2, 2):
        graph[nodes[i]].append(nodes[i+1])
    print('#{} {}'.format(tc, dfs(graph)))
