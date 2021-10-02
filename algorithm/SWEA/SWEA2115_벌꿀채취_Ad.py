T = int(input())

# 선택 가능한 모든 경우를 탐색하여, 각 경우에서의 최대 이익을 저장하여 list로 반환하는 함수
def all_search():
    profits = []
    # 모든 가능한 선택 경우에 대해서,
    for row in range(N):
        for col in range(N - M + 1):
            tmp = honeys[row][col:col + M]
            max_profit = -1
            # 선택한 경우가 가질 수 있는 모든 부분집합을 구하고
            for i in range(1 << M):
                case = []
                for j in range(M):
                    if i & (1 << j):
                        case.append(tmp[j])
                # 부분집합 원소의 합이 채집 가능한 꿀의 양을 넘지 않았으면,
                if sum(case) <= C:
                    temp_profit = 0
                    # 해당 경우에서의 이익을 구한다.
                    for num in case:
                        temp_profit += num ** 2
                    # 지금까지의 경우보다 이익이 큰 경우, 최대 이익을 바꿔준다.
                    if max_profit < temp_profit:
                        max_profit = temp_profit
            # row, col 지점을 선택했을 때의 최대 이익을 저장해준다.
            profits.append([max_profit, row, col])

    return profits


# 모든 가능한 경우의 수에서 최대 이익을 찾아 반환하는 함수
def find_best(cases):
    answer = 0
    c = len(cases)
    # 두 개를 택하는 모든 경우를 탐색
    for i in range(c - 1):
        for j in range(i, c):
            # 서로 다른 줄의 이익값을 택한 경우
            if cases[i][1] != cases[j][1]:
                # 채집 지점이 겹칠 수 없으므로 둘의 이익을 더한다.
                tmp = cases[i][0] + cases[j][0]
            # 서로 같은 줄을 택한 경우, 채집 지점이 겹쳤는지를 확인해야 한다.
            else:
                # 둘의 col 값의 차가, 탐색 길이(M)보다 크거나 같다면 겹치지 않은 것이므로,
                if cases[j][2] - cases[i][2] >= M:
                    # 둘의 이익을 더한다.
                    tmp = cases[i][0] + cases[j][0]
                # 만약 겹쳤다면, 이익을 낼 수 없으므로 continue
                else:
                    continue

            # 최대 이익을 계속해서 갱신해준다.
            if answer < tmp:
                answer = tmp

    return answer


for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]
    cases = all_search()
    print('#{} {}'.format(tc, find_best(cases)))
