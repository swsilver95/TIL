N = int(input())


def solution(N):
    for number in range(1000000):
        answer = number
        for num in str(number):
            answer += int(num)

        if answer == N:
            return number
        elif number >= N:
            return 0
    return 0


print(solution(N))
