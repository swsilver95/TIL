import sys
sys.stdin = open('input.txt')


def post_order(node):
    if node:
        post_order(tree[node][0])
        post_order(tree[node][1])
        formula.append(nodes[node])


def calculate(formula):
    stack = []
    for token in formula:
        if type(token) == int:
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N + 1)]
    nodes = [0 for _ in range(N + 1)]

    for _ in range(N):
        tmp = list(input().split())
        if tmp[1].isdigit():
            parent, num = int(tmp[0]), int(tmp[1])
            nodes[parent] = num
        else:
            parent, operator, left, right = int(tmp[0]), tmp[1], int(tmp[2]), int(tmp[3])
            nodes[parent] = operator
            tree[parent][0] = left
            tree[parent][1] = right
            tree[left][2] = parent
            tree[right][2] = parent

    formula = []
    post_order(1)
    print('#{} {}'.format(tc, calculate(formula)))