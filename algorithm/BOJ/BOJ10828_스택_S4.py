import sys
input = sys.stdin.readline

N = int(input())

stk = []
for _ in range(N):
    tmp = list(input().rstrip().split())
    if tmp[0] == 'push':
        stk.append(tmp[1])

    elif tmp[0] == 'top':
        if stk:
            print(stk[len(stk) - 1])
        else:
            print(-1)

    elif tmp[0] == 'size':
        print(len(stk))

    elif tmp[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)

    else:
        if stk:
            print(stk.pop())
        else:
            print(-1)
