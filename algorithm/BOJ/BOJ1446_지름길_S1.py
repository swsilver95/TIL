from heapq import *

N, D = map(int, input().split())

graph = [[] for _ in range(D + 1)]

for _ in range(N):
    start, end, length = map(int, input().split())

    if end > D:
        continue
    if end - start < length:
        continue

    graph[start].append((length, end))

for i in range(D):
    for j in range(i, D + 1):
        graph[i].append((j - i, j))

# print(graph)

INF = 1e9
distance = [INF] * (D+1)

heap = []
heappush(heap, (0, 0))

while heap:
    dist, node = heappop(heap)
    for next_dist, next_node in graph[node]:
        total_length = dist + next_dist
        if distance[next_node] > total_length:
            distance[next_node] = total_length
            heappush(heap, (total_length, next_node))

# print(distance)
print(distance[D])
