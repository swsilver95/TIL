import sys
import math

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    tmp = ''
    i = 0
    while True:
        i += 1
        N *= 2
        tmp += str(int(N))
        N -= int(N)
        if math.isclose(N, 0):
            break

        if i >= 13:
            tmp = 'overflow'
            break

    print('#{} {}'.format(tc, tmp))
