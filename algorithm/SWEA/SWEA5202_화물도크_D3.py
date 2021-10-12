import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = []
    for _ in range(N):
        s, e = map(int, input().split())
        data.append((s, e))

    data.sort(key=lambda x: (x[0], x[1]))

    end = data[0][1]
    cnt = 1
    if N >= 2:
        for i in range(0, N - 1):
            if end >= data[i + 1][1]:
                end = data[i + 1][1]
            else:
                if end <= data[i + 1][0]:
                    cnt += 1
                    end = data[i + 1][1]

    print('#{} {}'.format(tc, cnt))