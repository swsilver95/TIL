'''
from collections import deque
from itertools import permutations

T = int(input())


def calculate(x):
    q = deque(x)
    while len(q) > 1:
        a = q.popleft()
        b = q.popleft()
        c = q.popleft()
        # print(a + b + c)
        t = int(eval(a + b + c))
        q.appendleft(str(t))

    return int(q.pop())


for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(str, input().rstrip()))

    oper = '' + '+' * operators[0] + '-' * operators[1] + '*' * operators[2] + '/' * operators[3]
    cases = set(permutations(oper, N-1))
    # print(cases)
    # print(len(cases))
    max_num = -100000000
    min_num = 100000000
    for case in cases:
        tmp = numbers[:]
        for i in range(N - 1):
            tmp[2*i + 1] = case[i]
        result = calculate(tmp)
        if max_num < result:
            max_num = result
        if min_num > result:
            min_num = result

    print('#{} {}'.format(tc, max_num - min_num))
'''

T = int(input())


def dfs(idx, value):
    global max_num, min_num
    if idx == N - 1:
        if max_num < value:
            max_num = value
        if min_num > value:
            min_num = value
        return

    for i in range(4):
        if operators[i]:
            # 더하기
            if i == 0:
                operators[i] -= 1
                dfs(idx + 1, value + numbers[idx + 1])
                operators[i] += 1
            # 빼기
            elif i == 1:
                operators[i] -= 1
                dfs(idx + 1, value - numbers[idx + 1])
                operators[i] += 1
            # 곱하기
            elif i == 2:
                operators[i] -= 1
                dfs(idx + 1, value * numbers[idx + 1])
                operators[i] += 1
            # 나누기
            elif i == 3:
                operators[i] -= 1
                dfs(idx + 1, int(value / numbers[idx + 1]))
                operators[i] += 1


for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().rstrip().split()))
    max_num = -100000000
    min_num = 100000000
    dfs(0, numbers[0])
    print('#{} {}'.format(tc, max_num - min_num))