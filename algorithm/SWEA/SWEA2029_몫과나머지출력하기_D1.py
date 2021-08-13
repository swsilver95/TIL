def my_divmod(x, y):
    return(f'{x // y} {x % y}')

T = int(input())

for i in range(T):
    a, b = map(int, input().rstrip().split(' '))
    print(f'#{i + 1} {my_divmod(a, b)}')