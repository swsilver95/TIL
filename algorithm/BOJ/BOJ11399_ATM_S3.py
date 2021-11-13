N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
now = 0
answer = 0

for number in numbers:
    now += number
    answer += now

print(answer)


