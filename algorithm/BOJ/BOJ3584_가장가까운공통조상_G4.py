from collections import deque

T = int(input())


def bfs(root):
    visited = [0] * (N + 1)
    visited[root] = 1
    depth[root] = 1
    q = deque()
    q.append(root)

    while q:
        p = q.popleft()
        for node in graph[p]:
            if not visited[node]:
                visited[node] = visited[p] + 1
                depth[node] = visited[node]
                q.append(node)


def find_parent(node):
    return parents[node]


def find_root():
    for i in range(1, N + 1):
        if parents[i] == 0:
            return i


for tc in range(T):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    parents = [0] * (N + 1)
    depth = [0] * (N + 1)

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        graph[parent].append(child)
        # child 노드의 부모는 parent임을 저장
        parents[child] = parent

    n1, n2 = map(int, input().split())  # 공통조상을 찾아야 할 노드

    root_node = find_root()
    # print(parents)
    # print(root_node)
    bfs(root_node)
    # print(depth)

    dep1 = depth[n1]
    dep2 = depth[n2]

    # 두 노드의 깊이가 같아질 때까지,
    while dep1 != dep2:

        # n1의 깊이가 더 깊으면, n1의 깊이를 하나 줄이고 부모를 찾음
        if dep1 > dep2:
            n1 = find_parent(n1)
            dep1 = depth[n1]
        # n2의 깊이가 더 깊으면, n2의 깊이를 하나 줄이고 부모를 찾음
        elif dep1 < dep2:
            n2 = find_parent(n2)
            dep2 = depth[n2]

    # 그 결과 두 노드가 같다면, 공통부모를 찾은 것이다
    if n1 == n2:
        print(n1)
    # 같지 않다면, 두 노드의 부모를 찾고, 깊이를 하나씩 줄인다.
    else:
        while dep1 != 0 and dep2 != 0:
            n1 = find_parent(n1)
            n2 = find_parent(n2)
            dep1 = depth[n1]
            dep2 = depth[n2]

            # 깊이를 줄여가는 도중 두 노드가 같아지는 시점이 있다면 print
            if n1 == n2:
                print(n1)
                break


