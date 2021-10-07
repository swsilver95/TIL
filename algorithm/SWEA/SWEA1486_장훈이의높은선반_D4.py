T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    possible = [0]
    # DP
    for height in heights:
        p = len(possible)
        for i in range(p):
            possible.append(possible[i] + height)

    possible.sort()
    for j in range(len(possible)):
        if possible[j] >= B:
            print('#{} {}'.format(tc, possible[j] - B))
            break
