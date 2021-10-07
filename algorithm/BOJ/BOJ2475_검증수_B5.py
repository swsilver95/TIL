numbers = list(map(int, input().split()))

tmp = 0
for number in numbers:
    tmp += number ** 2

print(tmp % 10)