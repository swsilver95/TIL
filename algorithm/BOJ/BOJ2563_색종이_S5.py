import sys
input = sys.stdin.readline


paper = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())
cnt = 0
for _ in range(N):
    width, height = map(int, input().split())
    for h in range(10):
        for w in range(10):
            a = paper[height + h][width + w]
            if a == 0:
                paper[height + h][width + w] = 1
                cnt += 1
            else:
                continue

print(cnt)
