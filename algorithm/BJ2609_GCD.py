'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
첫째 줄에는 두 개의 자연수가 주어진다. 
이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 
둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

입력 예시 1)
24 18

출력 예시 1)
6
72

'''

a, b = map(int, input().split(" "))

def GCD(x, y):
    x_divisor = []
    y_divisor = []
    for i in range(1, x + 1):
        if x % i == 0:
            x_divisor.append(i)
    for j in range(1, y + 1):
        if y % j == 0:
            y_divisor.append(j)
    com_divisor = [a for a in x_divisor if a in y_divisor]
    return(max(com_divisor))

def LCM(x, y):
    a = x // GCD(x, y)
    b = y // GCD(x, y)
    return(a * b * GCD(x, y))



print(GCD(a, b))
print(LCM(a, b))