import sys

sys.stdin = open('input.txt')

T = int(input())

def find_palindrome(data, N, M):
    for i in range(N):
        for j in range(0, N - M + 1):
            if data[i][j:j+M+1] == data[i][j:j+M+1][::-1]:
                return ''.join(data[i][j:j+M+1])

    tp_data = list(zip(*data))
    for i in range(N):
        for j in range(0, N - M + 1):
            if tp_data[i][j:j+M+1] == tp_data[i][j:j+M+1][::-1]:
                return ''.join(tp_data[i][j:j+M+1])

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(str, input())) for _ in range(N)]

    print('#{} {}'.format(tc, find_palindrome(data, N, M)))