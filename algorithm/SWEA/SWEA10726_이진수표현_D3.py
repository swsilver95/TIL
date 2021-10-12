import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    answer = 'ON'
    for i in range(N):
        if not M & (1 << i):
            answer = 'OFF'
            break

    print('#{} {}'.format(tc, answer))

