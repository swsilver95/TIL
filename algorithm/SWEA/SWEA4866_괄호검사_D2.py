import sys
sys.stdin = open('input.txt')

T = int(input())

def balance(letters):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    stk = []
    for i in range(len(letters)):
        if (letters[i] not in left) and (letters[i] not in right):  # 괄호가 아니라면 확인할 필요가 없다.
            continue
        elif letters[i] in left:                                    # 여는 괄호가 나타나면 stack에 push
            stk.append(letters[i])
        else:                                                       # 닫는 괄호가 나타났을 때
            if not stk:                                             # 스택이 비어있다면 괄호가 안 맞는 것
                return 0

            if letters[i] == ')' and stk[-1] == '(':                # 현재 확인중인 값과 스택의 마지막 값이 같은 쌍일 경우
                stk.pop()                                           # 스택의 마지막 값을 제거
            elif letters[i] == ']' and stk[-1] == '[':
                stk.pop()
            elif letters[i] == '}' and stk[-1] == '{':
                stk.pop()
            else:
                return 0

    if stk:                                                         # 끝까지 확인한 뒤에 스택이 비어있지 않다면
        return 0                                                    # 괄호가 안 맞는 것
    else:
        return 1

for tc in range(1, T + 1):
    letters = input()
    print('#{} {}'.format(tc, balance(letters)))
