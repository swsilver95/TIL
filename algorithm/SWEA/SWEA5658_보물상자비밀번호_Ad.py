from collections import deque

T = int(input())


def rotate():
    a = numbers.pop()
    numbers.appendleft(a)
    return


def find_numbers(edge):
    for i in range(0, N, edge):
        j = 0
        tmp = ''
        while j < edge:
            tmp += numbers[i + j]
            j += 1
        # print(tmp)
        num = int(tmp, 16)
        answers.add(num)
    return


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    edge = N // 4
    numbers = deque(input())
    answers = set()

    # 0회전
    find_numbers(edge)

    r = 0
    while r < edge:
        rotate()
        find_numbers(edge)
        r += 1

    answers = list(answers)
    answers.sort(reverse=True)
    # print(answers)
    print('#{} {}'.format(tc, answers[K - 1]))