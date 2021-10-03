T = int(input())


def check_row(row_num, my_list):
    stk1 = []
    stk2 = []
    for col in range(N):
        # 스택2가 비어있으면
        if not stk2:
            # 스택1이 비어있으면
            if not stk1:
                stk1.append(my_list[row_num][col])
            else:
                if my_list[row_num][col] == stk1[-1]:
                    stk1.append(my_list[row_num][col])
                elif my_list[row_num][col] == stk1[-1] + 1:
                    if len(stk1) >= X:
                        stk1.clear()
                        stk1.append(my_list[row_num][col])
                    else:
                        return False
                elif my_list[row_num][col] == stk1[-1] - 1:
                    stk2.append(my_list[row_num][col])
                else:
                    return False
        # 스택2가 비어있지 않으면
        else:
            if my_list[row_num][col] == stk2[-1]:
                stk2.append(my_list[row_num][col])
            elif my_list[row_num][col] == stk2[-1] - 1:
                if len(stk2) >= X:
                    stk1.clear()
                    stk2.clear()
                    stk2.append(my_list[row_num][col])
                else:
                    return False
            elif my_list[row_num][col] == stk2[-1] + 1:
                if len(stk2) >= 2 * X:
                    stk1.clear()
                    stk2.clear()
                    stk1.append(my_list[row_num][col])
                    continue
                else:
                    return False
            else:
                return False
    if stk2:
        if len(stk2) >= X:
            return True
        else:
            return False
    else:
        return True


for tc in range(1, T + 1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    good_row = []
    good_col = []
    for i in range(N):
        if check_row(i, data):
            cnt += 1
            good_row.append(i)

    data_tp = list(zip(*data))
    for j in range(N):
        if check_row(j, data_tp):
            cnt += 1
            good_col.append(j)

    # print(data_tp)
    # print(good_row, good_col)
    print('#{} {}'.format(tc, cnt))