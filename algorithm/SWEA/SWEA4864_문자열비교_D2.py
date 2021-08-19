import sys

sys.stdin = open('input.txt')

T = int(input())

def find_letters(letters, pattern):
    for i in range(0, len(letters) - len(pattern) + 1):
        tmp = 0
        for j in range(len(pattern)):
            if letters[i+j] != pattern[j]:
                break
            else:
                tmp += 1
                if tmp == len(pattern):
                    return 1
    return 0


for tc in range(1, T + 1):
    pattern = input()
    letters = input()

    print('#{} {}'.format(tc, find_letters(letters, pattern)))