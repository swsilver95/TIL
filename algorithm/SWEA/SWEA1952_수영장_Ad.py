"""
1일 10원
1달 40원
3달 100원
1년 300원
"""

T = int(input())

for tc in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    schedule = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(13)]

    for month in range(1, 13):
        dp[month] = min(schedule[month] * d, m) + dp[month - 1]
        if month >= 3:
            dp[month] = min(dp[month], dp[month - 3] + m3)

    if dp[12] > y:
        ans = y
    else:
        ans = dp[12]

    print('#{} {}'.format(tc, ans))