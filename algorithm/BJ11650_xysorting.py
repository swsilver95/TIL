import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()
# print(data)

for i in data:
    print(' '.join(map(str, i)))