N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for number in numbers:
    if number < X:
        print(number, end=' ')