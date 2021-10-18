from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())


def dijkstra(start):
    heap = []
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


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2, cost = map(int, input().split())
    graph[n1].append((cost, n2))

for g in graph:
    g.sort()

start, end = map(int, input().split())

INF = 1e9
distance = [INF] * (N + 1)
dijkstra(start)
print(distance[end])
