import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

p1 = (0, 0)
p2 = (w, h)
p3 = (0, h)
p4 = (w, 0)

points = [p1, p2, p3, p4]

answer = 1001
for p in points:
    a, b = p
    answer = min(answer, abs(x-a), abs(y-b))

print(answer)
