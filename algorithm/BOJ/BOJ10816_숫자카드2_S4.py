N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cnt = [0] * 20000001
for number in numbers:
    cnt[number + 10000000] += 1

for target in targets:
    print(cnt[target + 10000000], end=' ')
