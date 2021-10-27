N = int(input())


def solution(N):
    i = 1
    while N > (3*i**2 - 3*i + 1):
        i += 1

    return i


print(solution(N))
