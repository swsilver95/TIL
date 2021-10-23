M, N = map(int, input().split())

check = [True] * (N + 1)
check[0] = False
check[1] = False

n = int(N ** 0.5)
for i in range(2, n + 1):
    if check[i]:
        for j in range(2 * i, N + 1, i):
            check[j] = False

for k in range(M, N + 1):
    if check[k]:
        print(k)


