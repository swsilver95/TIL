import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())


def is_uphill(number):
    a = number
    number = str(number)
    n = len(number)

    for i in range(n - 1):
        if number[i] > number[i + 1]:
            return -1

    return a


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers_comb = list(combinations(numbers, 2))
    nums = []
    for case in numbers_comb:
        i = case[0]
        j = case[1]
        nums.append(i * j)
    nums.sort()
    # print(nums)

    for i in range(len(nums)-1, -1, -1):
        uphill = is_uphill(nums[i])
        # print(uphill)
        if uphill > 0:
            break

    print('#{} {}'.format(tc, uphill))