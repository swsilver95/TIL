import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    pattern = input()
    pattern = list(set(pattern))
    letters = input()

    cnt = 0
    for pat in pattern:
        tmp = letters.count(pat)
        cnt = max(cnt, tmp)

    print('#{} {}'.format(tc, cnt))