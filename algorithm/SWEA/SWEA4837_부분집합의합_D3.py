import sys

sys.stdin = open('input.txt')

numbers = list(range(1, 13))

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    tot_cnt = 0
    for i in range(1<<12):
        cnt = 0
        tmp = 0
        for j in range(12):
            if i & (1<<j):
                tmp += numbers[j]
                cnt += 1
        if cnt == N and tmp == K:
            tot_cnt += 1

    print('#{} {}'.format(tc, tot_cnt))