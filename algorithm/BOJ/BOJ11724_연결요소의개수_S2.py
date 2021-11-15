# from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

# 1. bfs 풀이 방식
# graph = [[] for _ in range(N + 1)]
#
# for _ in range(M):
#     n1, n2 = map(int, input().split())
#     graph[n1].append(n2)
#     graph[n2].append(n1)
#
#
# visited = [0] * (N + 1)
#
#
# def bfs(node):
#     visited[node] = 1
#     q = deque()
#     q.append(node)
#
#     while q:
#         p = q.popleft()
#         for next_p in graph[p]:
#             if not visited[next_p]:
#                 q.append(next_p)
#                 visited[next_p] = 1
#
#
# cnt = 0
# for i in range(1, N + 1):
#     if not visited[i]:
#         bfs(i)
#         cnt += 1
#
# print(cnt)

# 2. Union Find

parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        pass


for _ in range(M):
    n1, n2 = map(int, input().split())
    union(n1, n2)

cnt = set()
for node in range(1, N + 1):
    cnt.add(find(node))

# print(parent)
# print(cnt)
print(len(cnt))
