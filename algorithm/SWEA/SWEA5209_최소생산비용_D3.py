import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(idx, total):
    global answer
    if idx == N:
        if answer > total:
            answer = total
        return

    if answer < total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(idx + 1, total + price[idx][i])
            visited[i] = False


for tc in range(1, T + 1):
    N = int(input())
    price = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    answer = 1500
    dfs(0, 0)
    print('#{} {}'.format(tc, answer))