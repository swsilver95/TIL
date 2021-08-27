import sys
sys.stdin = open('input.txt')
'''
1 - 빨간색(S극에 끌림, 아래로 향함)
2 - 파란색(N극에 끌림, 위로 향함)
'''
for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    total = 0
    for col in range(100):
        stack = []
        for row in range(100):
            if table[row][col] == 0:
                continue

            if len(stack) == 0:                                     # 1. 스택이 비어있을 때
                if table[row][col] == 2:                            # 1-1. 파란색을 만나면,
                    continue                                        # => 책상 밖으로 떨어지므로 continue
                elif table[row][col] == 1:                          # 1-2. 빨간색을 만나면,
                    stack.append('N')                               # => 스택에 푸시
            else:                                                   # 2. 스택이 비어있지 않을 때
                if table[row][col] == 1 and stack[-1] == 'S':       # 2-1. 스택의 마지막값이 파란색이고 빨간색을 만나면,
                    stack.clear()                                   # => 하나의 교착상태가 앞서 만들어진다는 뜻이므로 스택을 비워주고
                    stack.append('N')                               # => 빈 스택에 다시 N을 푸시
                    total += 1                                      # => 교착점 개수를 한 개 더해줌
                elif table[row][col] == 1 and stack[-1] == 'N':     # 2-2. 스택의 마지막값이 빨간색인 상태로 빨간색을 만나면,
                    stack.append('N')                               # => 아직 교착점이 되지 않았으므로 스택에 푸시
                else:                                               # 2-3. 파란색을 만나면
                    stack.append('S')                               # => 스택에 푸시

        if stack:                                                   # 3. S 다음 N이 나오는 것을 기준으로 교착점을 셌으므로,
            if stack[-1] == 'S':                                    # 3-1. 스택의 마지막값이 S로 끝난 경우에는 교착점이 하나 더 있는 것
                total += 1                                          # 3-2. 따라서 교착점 개수에 하나를 추가

    print('#{} {}'.format(tc, total))