import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(stop, cnt):
    global answer
    if stop == N:
        if answer > cnt:
            answer = cnt
        return

    if cnt > answer:
        return

    charge = battery[stop]
    for s in range(stop + charge, stop, -1):
        if s <= N:
            if not visited[s]:
                visited[s] = True
                dfs(s, cnt + 1)
                visited[s] = False


for tc in range(1, T + 1):
    N, *battery = map(int, input().split())
    battery = [0] + battery
    visited = [False] * (N + 1)
    visited[1] = True
    answer = 101
    dfs(1, 0)
    print('#{} {}'.format(tc, answer - 1))