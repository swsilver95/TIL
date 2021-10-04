import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

data = {}

for _ in range(N):
    site, pw = map(str, input().rstrip().split())
    data[site] = pw

for _ in range(M):
    target = input().rstrip()
    print(data[target])