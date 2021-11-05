import sys
input = sys.stdin.readline

M, N = map(int, input().split())
numbers = list(map(int, input().split()))
acc_numbers = [0] * M
acc_numbers[0] = numbers[0]
for i in range(1, M):
    acc_numbers[i] = acc_numbers[i - 1] + numbers[i]

# print(acc_numbers)
for _ in range(N):
    start, end = map(int, input().split())
    if start == 1:
        answer = acc_numbers[end - 1]
    else:
        answer = acc_numbers[end - 1] - acc_numbers[start - 2]
    print(answer)
