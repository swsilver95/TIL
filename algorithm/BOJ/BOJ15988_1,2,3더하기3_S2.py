T = int(input())


def solution(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    if n == 4:
        return 7

    answer = [1, 2, 4, 7]
    i = 5
    while i <= n:
        answer = [answer[1], answer[2], answer[3], (answer[1] + answer[2] + answer[3]) % 1000000009]
        i += 1

    return answer[3]


for tc in range(T):
    N = int(input())
    print(solution(N))
