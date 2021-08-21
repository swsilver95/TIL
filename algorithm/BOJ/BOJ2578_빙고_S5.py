import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
check = [[False for _ in range(5)] for _ in range(5)]
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))


def check_bingo(check):
    tp_check = list(zip(*check))
    bingo_count = 0
    tmp_check1 = True
    tmp_check2 = True
    for row in range(5):
        # 가로/세로 빙고 확인
        if all(check[row]):
            bingo_count += 1

        if all(tp_check[row]):
            bingo_count += 1

        # 대각선 확인
        tmp_check1 *= check[row][row]
        tmp_check2 *= check[row][4 - row]

    if tmp_check1:
        bingo_count += 1

    if tmp_check2:
        bingo_count += 1

    if bingo_count >= 3:
        return True
    else:
        return False


def start_bingo(numbers):
    cnt = 0
    for number in numbers:
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == number:
                    cnt += 1
                    check[i][j] = True

                    if check_bingo(check):
                        return cnt


print(start_bingo(numbers))


