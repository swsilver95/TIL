import sys
from collections import deque
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    numbers = deque(list(map(int, input().split())))
    # print(numbers)
    N = 8
    i = 1
    while True:
        left = numbers.popleft() - i
        if left <= 0:
            left = 0
            numbers.append(0)
            break
        numbers.append(left)
        i += 1
        if i == 6:
            i = 1

    print('#{}'.format(tc), end=' ')
    for _ in range(8):
        print(numbers.popleft(), end=' ')
    print()