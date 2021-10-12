import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weights.sort(reverse=True)
    trucks.sort(reverse=True)
    check = [False] * N
    answer = 0

    t = 0
    while t < M:
        for i in range(N):
            if trucks[t] >= weights[i] and not check[i]:
                answer += weights[i]
                check[i] = True
                break
        t += 1

    print('#{} {}'.format(tc, answer))