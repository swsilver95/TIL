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
    n = len(my_str)
    for i in range(n):
        if my_str[i].isalpha():
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


text = input()
postfix = infix_to_postfix(text)
print(postfix)