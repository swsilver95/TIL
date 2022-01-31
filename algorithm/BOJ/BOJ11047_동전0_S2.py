N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

ans = 0
for coin in coins:
    ans += K // coin
    K %= coin
    if K == 0:
        break

print(ans)
