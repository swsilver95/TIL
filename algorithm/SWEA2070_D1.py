T = int(input())
data = []
for _ in range(T):
    data.append(list(map(int, input().strip().split(' '))))

def large_or_small(numbers):
    a = numbers[0]
    b = numbers[1]
    if a > b:
        return('>')
    elif a < b:
        return('<')
    else:
        return('=')

for i in range(T):
    print(f'#{i + 1} {large_or_small(data[i])}')