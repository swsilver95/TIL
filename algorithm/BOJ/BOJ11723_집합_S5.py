import sys
input = sys.stdin.readline

M = int(input().rstrip())

S = set()

for _ in range(M):
    tmp = input().rstrip()
    if tmp == 'all':
        S = set(range(1, 21))
        continue
    elif tmp == 'empty':
        S.clear()
        continue

    command, num = tmp.split()
    num = int(num)

    if command == 'add':
        if num in S:
            continue
        else:
            S.add(num)

    elif command == 'check':
        if num in S:
            print(1)
        else:
            print(0)

    elif command == 'remove':
        if num in S:
            S.remove(num)
        else:
            pass

    elif command == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)

