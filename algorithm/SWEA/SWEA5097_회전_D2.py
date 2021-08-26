import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    i = 0
    while i < M:
        i += 1
        q.append(q.pop(0))

    print('#{} {}'.format(tc, q[0]))