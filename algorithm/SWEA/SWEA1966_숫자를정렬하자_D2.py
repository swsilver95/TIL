T = int(input())

for idx in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'#{idx+1}', end=' ')
    print(' '.join(map(str, numbers)))
