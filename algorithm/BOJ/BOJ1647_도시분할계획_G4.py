import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    else:
        parent[x] = y


def kruskal(edges):
    global answer, max_cost
    for edge in edges:
        cost, n1, n2 = edge
        if find(n1) != find(n2):
            union(n1, n2)
            answer += cost
            if max_cost < cost:
                max_cost = cost


N, M = map(int, input().split())
edges = []
for _ in range(M):
    n1, n2, w = map(int, input().rstrip().split())
    edges.append((w, n1, n2))

# 부모를 자기 자신으로 초기화
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

# 크루스칼 알고리즘에서는 정렬이 필수
edges.sort()
answer = 0
max_cost = 0

kruskal(edges)
print(answer - max_cost)
