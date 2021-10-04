N = int(input())

numbers = list(map(int, input().split()))

max_num = -1000001
min_num = 1000001
for i in range(len(numbers)):
    if max_num < numbers[i]:
        max_num = numbers[i]

    if min_num > numbers[i]:
        min_num = numbers[i]


print(min_num, max_num)