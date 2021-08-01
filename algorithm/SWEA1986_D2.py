T = int(input())
for idx in range(T):
    print(f'#{idx + 1}', end=' ')
    num = int(input())
    total = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            total -= i
        else:
            total += i
    print(total)