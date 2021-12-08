N = int(input())
stairs = [0] * 301
dp = [0] * 301

for i in range(N):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for j in range(3, N):
    dp[j] = max(dp[j - 3] + stairs[j - 1] + stairs[j], dp[j - 2] + stairs[j])

print(dp[N - 1])
