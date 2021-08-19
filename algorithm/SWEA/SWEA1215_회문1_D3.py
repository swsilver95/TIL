import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    data = [list(map(str, input())) for _ in range(8)]
    tp_data = list(zip(*data))

    cnt = 0
    for i in range(8):
        for j in range(0, 9 - n):
            if data[i][j:j+n] == data[i][j:j+n][::-1]:
                cnt += 1

        for k in range(0, 9 - n):
            if tp_data[i][k:k + n] == tp_data[i][k:k + n][::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))