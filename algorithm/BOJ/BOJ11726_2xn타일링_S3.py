n = int(input())


def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3

    i = 4
    my_list = [2, 3]
    while i <= n:
        my_list = [my_list[1], my_list[0] + my_list[1]]
        i += 1

    return my_list[1]


print(solution(n) % 10007)
