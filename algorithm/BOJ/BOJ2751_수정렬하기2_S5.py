from heapq import *
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

heap = []
for _ in range(N):
    heappush(heap, int(input().rstrip()))

while heap:
    print(str(heappop(heap)) + '\n')