import sys
input = sys.stdin.readline


N = int(input())
cnt = [0] * 10001
for _ in range(N):
    cnt[int(input().rstrip())] += 1

idx = 1
c = 0
while idx <= 10000 and c <= N:
    if cnt[idx] != 0:
        cnt[idx] -= 1
        c += 1
        print(idx)
    else:
        idx += 1

