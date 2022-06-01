import sys
input = sys.stdin.readline

T = int(input())


def solution(n):
    ans = [1, 1, 1, 2, 2, 3]

    if n <= 6:
        return ans[n - 1]

    for i in range(6, n):
        ans.append(ans[i - 3] + ans[i - 2])

    return ans[n - 1]


for tc in range(T):
    N = int(input())
    print(solution(N))


