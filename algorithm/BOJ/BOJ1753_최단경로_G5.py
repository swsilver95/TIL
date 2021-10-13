from heapq import *
import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
K = int(input().rstrip())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((w, v))

# 시간 복잡도를 줄이기 위한 그래프 내부 정렬
for g in graph:
    g.sort()

INF = 1e9
distance = [INF] * (V + 1)
distance[K] = 0


def dijkstra(start):
    heap = list()
    # 시작 노드까지의 거리를 0으로 초기화해두고 시작
    heappush(heap, (0, start))
    # 모든 노드의 거리를 INF로 초기화

    while heap:
        d, node = heappop(heap)

        for next_d, next_node in graph[node]:
            from_start = d + next_d
            if distance[next_node] > from_start:
                distance[next_node] = from_start
                heappush(heap, (from_start, next_node))


dijkstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])