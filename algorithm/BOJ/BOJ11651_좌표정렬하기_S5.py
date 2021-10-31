import sys
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda i: (i[1], i[0]))

for point in points:
    print(*point)
