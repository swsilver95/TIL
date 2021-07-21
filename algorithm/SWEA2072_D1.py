data = []
T = int(input())
for _ in range(T):
    data.append(list(map(int, input().split(' '))))

def list_odd_sum(my_list):
    total = 0
    for i in my_list:
        if i % 2 == 1:
            total += i
    return(total)

for j in range(1, T + 1):
    print(f'#{j} {list_odd_sum(data[j - 1])}')