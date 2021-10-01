T = int(input())


def dfs(cnt):
    global answer
    if cnt >= N:
        answer = max(answer, int(''.join(map(str, numbers))))
        return

    else:
        for i in range(M - 1):
            for j in range(i + 1, M):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                num = int(''.join(map(str, numbers)))
                if (num, cnt) not in visited:
                    visited.add((num, cnt))
                    dfs(cnt + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]


for tc in range(1, T + 1):
    tmp, N = map(str, input().strip().split())
    N = int(N)
    M = len(tmp)
    numbers = list(map(int, tmp))
    visited = set()
    answer = 0
    dfs(0)
    print('#{} {}'.format(tc, answer))
