from itertools import combinations, product
T = int(input())
'''
0 : A
1 : B
'''


def passed(idx):
    line = ''
    for row in range(D):
        line += str(film[row][idx])

    if t1 in line or t2 in line:
        return True
    else:
        return False


def change_level(row, x):
    for col in range(W):
        film[row][col] = x
    return


# def solution(repeat):
#     # 바꾸는 줄 수가 0줄인 경우, 바로 확인
#     if repeat == 0:
#         for col in range(W):
#             if not passed(col):
#                 # 성립이 안 되면 1줄을 바꿀 수 있도록 재귀
#                 return solution(repeat + 1)
#         # 안 바꿔도 되는 경우에는 0 리턴
#         else:
#             return 0
#     # 바꾸는 줄 수가 있는 경우
#     else:
#         cases = list(combinations(idx_list, repeat))
#         # 바꾸는 줄의 경우의 수 중에서 하나를 뽑아서
#         for case in cases:
#             # 해당 줄을 다 바꿔주고
#             for line_num, x in case:
#                 change_level(line_num, x)
#
#             # 바꾼 뒤에 검사를 다시 실시
#             for col in range(W):
#                 # 한 줄이라도 테스트 통과를 못하면 break
#                 if not passed(col):
#                     break
#             # 테스트를 모두 통과하면 바꾼 줄 수를 반환
#             else:
#                 return repeat
#
#             # 테스트를 통과하지 못하면 원상복구
#             for line_num, x in case:
#                 for col in range(W):
#                     film[line_num][col] = tmp[line_num][col]
#
#         # repeat 개수만큼의 줄을 바꿔서 해결이 안 된다면
#         # 한 줄을 더 바꾸는 경우를 탐색
#         return solution(repeat + 1)

def solution():
    for col in range(W):
        if not passed(col):
            break
    else:
        return 0

    # D줄에 대해서
    for pick in range(1, D + 1):
        cases = list(combinations(list(range(D)), pick))
        selects = list(product([0, 1], repeat=pick))
        for case in cases:
            for select in selects:
                for idx, line_num in enumerate(case):
                    change_level(line_num, select[idx])

                for col in range(W):
                    if not passed(col):
                        break
                else:
                    return pick

                for line_num in case:
                    for col in range(W):
                        film[line_num][col] = tmp[line_num][col]


for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    tmp = [r[:] for r in film]
    t1 = '0' * K
    t2 = '1' * K

    if K == 1:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, solution()))
