N = int(input())
n = 1003002

check = [True] * n
check[0] = False
check[1] = False
m = round(int(n ** 0.5))

for i in range(2, m + 1):
    if check[i]:
        for j in range(i + i, n, i):
            check[j] = False


def is_pal(num):
    tmp = str(num)
    if tmp == tmp[::-1]:
        return True
    return False


def solution(b):
    for k in range(b, n):
        if check[k] and is_pal(k):
            print(k)
            return


solution(N)
# dd
