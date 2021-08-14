T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    # print(stops)

    cnt = [0] * 5001
    for i in data:
        for j in range(i[0], i[1] + 1):
            cnt[j] += 1
    
    print('#{}'.format(tc), end=' ')
    for stop in stops:
        print(cnt[stop], end=' ')
    print()