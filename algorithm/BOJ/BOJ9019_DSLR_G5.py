"""
D | 2n % 10000
S | n-1 , n이 0이라면 9999
L | abcd를 bcda로 만듦
R | abcd를 dabc로 만듦
"""
from collections import deque
import sys
input = sys.stdin.readline


T = int(input())


def bfs(s, e):
    visited = [''] * 10000
    check = [False] * 10000
    check[s] = True
    q = deque()
    q.append(s)
    commands = ['D', 'S', 'L', 'R']

    while q:
        p = q.popleft()
        if p == e:
            return visited[p]

        # DSLR 연산
        D = (2 * p) % 10000
        S = (p - 1) % 10000
        L = (p * 10 + (p // 1000)) % 10000
        R = (p // 10 + (p % 10) * 1000) % 10000

        calc = [D, S, L, R]

        for d in range(4):
            next_p = calc[d]
            if not check[next_p]:
                check[next_p] = True
                q.append(next_p)
                visited[next_p] += visited[p] + commands[d]


for _ in range(T):
    start, end = map(int, input().split())
    print(bfs(start, end))
