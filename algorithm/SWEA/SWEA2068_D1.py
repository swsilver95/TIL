T = int(input())
data = []
for _ in range(T):
    data.append(list(map(int, input().rstrip().split(' '))))

def my_max(numbers):
    tmp = numbers[0]
    for number in numbers:
        if tmp <= number:
            tmp = number
    return(tmp)

for i in range(T):
    print(f'#{i + 1} {my_max(data[i])}')