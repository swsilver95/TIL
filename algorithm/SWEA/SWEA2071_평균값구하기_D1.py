T = int(input())
data = []
for _ in range(T):
    data.append(list(map(int, input().split(' '))))

def avg(numbers):
    total = 0
    for number in numbers:
        total += number
    return(total / len(numbers))

for i in range(T):
    print(f'#{i + 1} {round(avg(data[i]))}')