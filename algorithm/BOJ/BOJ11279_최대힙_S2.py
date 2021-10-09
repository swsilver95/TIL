import heapq
import sys
input = sys.stdin.readline


N = int(input().rstrip())
heap = []

for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, -x)