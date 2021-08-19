import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        idx = i
        for j in range(i, N):
            if i % 2 == 0:                                      # 만약 i가 0이거나 짝수라면
                if numbers[idx] < numbers[j]:                   # 최댓값을 가지는 인덱스를 찾고
                    idx = j
            else:                                               # 만약 i가 홀수라면
                if numbers[idx] > numbers[j]:                   # 최솟값을 가지는 인덱스를 찾아서
                    idx = j

        numbers[i], numbers[idx] = numbers[idx], numbers[i]     # 각 위치에 맞게 인덱스 교체 방식으로 정렬

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(numbers[i], end=' ')
    print()