# import sys

# sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]     # 배열의 길이는 100X100으로 고정

    max_num = sum(arr[0])           # 초기값을 지정
    for i in range(100):            # 1. 가로합 살펴보기
        total = 0
        for j in range(100):
            total += arr[i][j]
        if max_num < total:
            max_num = total

    for j in range(100):            # 2. 세로합 살펴보기
        total = 0
        for i in range(100):
            total += arr[i][j]
        if max_num < total:
            max_num = total

    total = 0
    for i in range(100):            # 3. 왼쪽 위 - 오른쪽 아래 대각선 합
        total += arr[i][i]
    if max_num < total:
        max_num = total


    total = 0
    for i in range(100):            # 4. 오른쪽 위 - 왼쪽 아래 대각선 합
        total += arr[99 - i][i]
    if max_num < total:
        max_num = total

    print('#{} {}'.format(tc, max_num))