from itertools import permutations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    idx = list(range(1, N))
    cases = list(permutations(idx, N - 1))

    battery = 1001
    for case in cases:
        tmp = data[0][case[0]] + data[case[N - 2]][0]
        for i in range(1, N - 1):
            tmp += data[case[i - 1]][case[i]]

        if battery > tmp:
            battery = tmp

    print('#{} {}'.format(tc, battery))