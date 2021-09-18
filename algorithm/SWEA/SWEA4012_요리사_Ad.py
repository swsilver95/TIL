from itertools import combinations

T = int(input())


def taste(selection, S):
    all_synergy = list(combinations(selection, 2))
    tastepoint = 0
    for synergy in all_synergy:
        x, y = synergy
        tastepoint += S[x][y]
        tastepoint += S[y][x]

    return tastepoint


for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    sel = list(range(N))
    cases = list(combinations(sel, N//2))
    diff = 99999999999

    for case in cases:
        food1 = set(case)
        food2 = set(sel) - food1
        taste1 = taste(food1, S)
        taste2 = taste(food2, S)
        tmp_diff = abs(taste1 - taste2)
        if diff > tmp_diff:
            diff = tmp_diff

    print('#{} {}'.format(tc, diff))