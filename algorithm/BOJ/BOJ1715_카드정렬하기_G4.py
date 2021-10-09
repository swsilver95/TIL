import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())


heap = []
for _ in range(N):
    heapq.heappush(heap, int(input().rstrip()))

# print(heap)
answer = 0
while len(heap) > 1:
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    answer += n1 + n2
    heapq.heappush(heap, n1 + n2)

print(answer)
