import sys
sys.stdin = open('input.txt')


def infix_to_postfix(my_str):
    isp = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0,
    }
    postfix = ''
    stack = []
    global n
    for i in range(n):
        if my_str[i].isdigit():
            postfix += my_str[i]
        else:
            if my_str[i] == '(':
                stack.append(my_str[i])
            elif my_str[i] == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack and isp.get(stack[-1]) >= isp.get(my_str[i]):
                    postfix += stack.pop()
                stack.append(my_str[i])

    while stack:
        postfix += stack.pop()

    return postfix


def calculate_postfix(ans):
    stack = []
    n = len(ans)
    for i in range(n):
        if ans[i].isdigit():
            stack.append(ans[i])
        else:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            if ans[i] == '*':
                stack.append(int(tmp2) * int(tmp1))
            elif ans[i] == '+':
                stack.append(int(tmp2) + int(tmp1))
            elif ans[i] == '-':
                stack.append(int(tmp2) - int(tmp1))
            elif ans[i] == '/':
                stack.append(int(tmp2) / int(tmp1))
    return stack.pop()


for tc in range(1, 11):
    n = int(input())
    text = input()
    postfix = infix_to_postfix(text)
    print(postfix, '--postfix')
    print('#{} {}'.format(tc, calculate_postfix(postfix)))
