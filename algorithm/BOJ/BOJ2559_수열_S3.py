import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))


def high_sum(numbers):
    global N
    global K
    high_tmp = 0
    for i in range(K):
        high_tmp += numbers[i]

    max_tmp = high_tmp
    for i in range(K, N):
        high_tmp = high_tmp - numbers[i - K] + numbers[i]
        max_tmp = max(max_tmp, high_tmp)

    return max_tmp


print(high_sum(temps))
