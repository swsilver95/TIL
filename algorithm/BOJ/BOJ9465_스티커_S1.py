import sys
input = sys.stdin.readline

T = int(input())


def solution(n):
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n == 1:
        return max(dp[0][0], dp[1][0])

    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
    if n == 2:
        return max(dp[0][1], dp[1][1])

    i = 2
    while i < N:
        dp[0][i] = stickers[0][i] + max(dp[1][i - 2], dp[1][i - 1])
        dp[1][i] = stickers[1][i] + max(dp[0][i - 2], dp[0][i - 1])
        i += 1

    return max(dp[0][n - 1], dp[1][n - 1])


for tc in range(T):
    N = int(input())
    stickers = [list(map(int, input().rstrip().split())) for _ in range(2)]
    print(solution(N))


