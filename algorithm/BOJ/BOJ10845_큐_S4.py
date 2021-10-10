from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    tmp = list(input().rstrip().split())

    if tmp[0] == 'push':
        q.append(tmp[1])
    else:
        if tmp[0] == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)

        elif tmp[0] == 'size':
            print(len(q))
        elif tmp[0] == 'empty':
            if not q:
                print(1)
            else:
                print(0)
        elif tmp[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif tmp[0] == 'back':
            if q:
                print(q[len(q) - 1])
            else:
                print(-1)