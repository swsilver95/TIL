import sys

sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    num_min = numbers[0]
    for number in numbers:
        if num_min > number:
            num_min = number

    num_max = numbers[0]
    for number in numbers:
        if num_max < number:
            num_max = number

    print('#{} {}'.format(idx, num_max - num_min))
