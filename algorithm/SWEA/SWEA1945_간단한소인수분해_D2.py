import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    number = int(input())
    a = b = c = d = e = 0               # a~e를 모두 0으로 초기화
    while number > 1:                   # number가 1보다 큰 동안에는 소인수분해가 가능
        if number % 11 == 0:            # 11의 배수이면 11로 나눠주고 e를 1 증가시킴
            number /= 11
            e += 1
        elif number % 7 == 0:           # 7의 배수이면 11로 나눠주고 e를 1 증가시킴
            number /= 7
            d += 1
        elif number % 5 == 0:           # 5의 배수이면 11로 나눠주고 e를 1 증가시킴
            number /= 5
            c += 1
        elif number % 3 == 0:           # 3의 배수이면 11로 나눠주고 e를 1 증가시킴
            number /= 3
            b += 1
        elif number % 2 == 0:           # 2의 배수이면 11로 나눠주고 e를 1 증가시킴
            number /= 2
            a += 1

    print('#{}'.format(tc), end=' ')
    print(a, b, c, d, e)