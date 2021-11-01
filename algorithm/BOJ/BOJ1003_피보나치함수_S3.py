T = int(input())

dp = [[1, 0], [0, 1], [1, 1]]  # 0, 1, 2

i = 3
while i < 41:
    dp.append([dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]])
    i += 1

for tc in range(T):
    N = int(input())
    print(*dp[N])

