T = int(input())

for idx in range(T):
    flag = True
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    
    # 1. 가로줄에 겹치는 숫자가 없는지
    for horizontal_line in sudoku:
        test = set(horizontal_line)
        if len(test) == 9:
            continue
        else:
            flag = False
            break

    # 2. 세로줄에 겹치는 숫자가 없는지
    for vertical_line in list(zip(*sudoku)):
        test = set(vertical_line)
        if len(test) == 9:
            continue
        else:
            flag = False
            break
    
    # 3. 9개의 영역에 겹치는 숫자가 없는지
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = [
                sudoku[i][j:j+3],
                sudoku[i+1][j:j+3],
                sudoku[i+2][j:j+3]
            ]
            tmp_list = sum(tmp, [])
            if len(set(tmp_list)) == 9:
                continue
            else:
                flag = False
                break
    print(f'#{idx + 1}', end=' ')
    if flag:
        print(1)
    else:
        print(0)