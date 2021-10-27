from collections import deque

T = int(input())


def solution():
    high = max(q)[0]
    cnt = 0
    while q:
        priority, order = q.popleft()
        if priority != high:
            q.append((priority, order))
        else:
            if order == M:
                cnt += 1
                break
            else:
                cnt += 1
                high = max(q)[0]

    return cnt


for tc in range(T):
    N, M = map(int, input().split())
    q = deque()
    numbers = list(map(int, input().split()))
    for i in range(N):
        q.append((numbers[i], i))

    print(solution())

