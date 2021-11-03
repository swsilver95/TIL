import sys
import itertools
sys.stdin = open('input2.txt', 'r')

T = int(input())


def is_available(line1, line2):
    s1, e1 = line1
    s2, e2 = line2
    flag = True
    # 출발, 도착점에 방향이 없음에 유의
    if abs(s1 - s2) <= 1 or abs(s1 - s2) == N - 1 or abs(e1 - e2) <= 1 or abs(e1 - e2) == N - 1:
        flag = False
    if abs(s1 - e1) <= 1 or abs(s1 - e1) == N - 1 or abs(s2 - e2) <= 1 or abs(s2 - e2) == N - 1:
        flag = False
    if abs(s1 - e2) <= 1 or abs(s1 - e2) == N - 1 or abs(s2 - e1) <= 1 or abs(s2 - e1) == N - 1:
        flag = False

    return flag


def calculate(line1, line2):
    s1, e1 = line1
    s2, e2 = line2
    value = (s1 + e1) ** 2 + (s2 + e2) ** 2

    return value


for tc in range(1, T + 1):
    N = int(input())
    stops = list(map(int, input().split()))
    sel = list(range(N))
    cases = itertools.combinations(sel, 4)
    answer = 0
    for case in cases:
        # 겹치지 않게 잇는 경우 1
        s1, s2, e2, e1 = case
        if is_available((s1, e1), (s2, e2)):
            value = calculate((stops[s1], stops[e1]), (stops[s2], stops[e2]))
            if answer < value:
                answer = value

        # 겹치지 않게 잇는 경우 2
        s1, e1, s2, e2 = case
        if is_available((s1, e1), (s2, e2)):
            value = calculate((stops[s1], stops[e1]), (stops[s2], stops[e2]))
            if answer < value:
                answer = value

    print('#{} {}'.format(tc, answer))

