T = int(input())
for idx in range(T):
    print(f'#{idx + 1}', end=' ')
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(int(round(sum(numbers[1:9])/8)))