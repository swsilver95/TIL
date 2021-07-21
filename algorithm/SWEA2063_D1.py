N = int(input())
numbers = list(map(int, input().rstrip().split(' ')))

for i in numbers:
    count_up = 0
    count_down = 0
    for j in numbers:
        if i > j:
            count_up += 1
        elif i < j:
            count_down += 1
    if count_up == count_down:
        print(i)
        break