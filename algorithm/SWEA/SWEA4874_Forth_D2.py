import sys

sys.stdin = open('input.txt')

T = int(input())


def calculate_postfix(formula):
    stack = []
    try:
        for token in formula:
            if token.isdigit():
                stack.append(token)
            elif token == '.':
                if len(stack) != 1:
                    return 'error'
                else:
                    return int(stack.pop())
            else:
                tmp2 = stack.pop()
                tmp1 = stack.pop()
                if token == '+':
                    stack.append(int(tmp1) + int(tmp2))
                elif token == '-':
                    stack.append(int(tmp1) - int(tmp2))
                elif token == '*':
                    stack.append(int(tmp1) * int(tmp2))
                elif token == '/':
                    stack.append(int(tmp1) // int(tmp2))
    except (IndexError, TypeError, ValueError):
        return 'error'


for tc in range(1, T + 1):
    formula = list(map(str, input().split()))
    print('#{} {}'.format(tc, calculate_postfix(formula)))
