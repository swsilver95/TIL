import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]

answer = 2501
for row in range(N - 8 + 1):
    for col in range(M - 8 + 1):
        case_W = 0
        case_B = 0
        for i in range(8):
            for j in range(8):
                # case_W / 흰색부터 시작하는 경우
                # 짝수번째 줄에서는 W부터 시작
                if i % 2 == 0:
                    # 컬럼 번호가 짝수일 때 'W'가 아니라면 바꿔야 함
                    if j % 2 == 0:
                        if board[row + i][col + j] != 'W':
                            case_W += 1
                        else:
                            case_B += 1
                    # 컬럼 번호가 홀수일 때 'B'가 아니라면 바꿔야 함
                    elif j % 2 == 1:
                        if board[row + i][col + j] != 'B':
                            case_W += 1
                        else:
                            case_B += 1
                # 홀수번째 줄에서는 B부터 시작
                else:
                    # 컬럼 번호가 짝수일 때 'B'가 아니라면 바꿔야 함
                    if j % 2 == 0:
                        if board[row + i][col + j] != 'B':
                            case_W += 1
                        else:
                            case_B += 1
                    # 컬럼 번호가 홀수일 때 'W'가 아니라면 바꿔야 함
                    elif j % 2 == 1:
                        if board[row + i][col + j] != 'W':
                            case_W += 1
                        else:
                            case_B += 1

        answer = min(answer, case_B, case_W)

print(answer)
