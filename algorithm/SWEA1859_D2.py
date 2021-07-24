T = int(input())
d = []
datum = []
for _ in range(T):
    d.append(int(input().rstrip()))
    datum.append(list(map(int, input().split(' '))))

def money(total, my_list):
    if len(my_list) <= 1:
        return total

    earn = total
    price_max = max(my_list)
    idx = my_list.index(price_max)
    buy_list = my_list[:idx + 1]
    # print(buy_list)
    earn += len(buy_list) * price_max - sum(buy_list)
    # print(earn)
    if len(buy_list) == len(my_list):
        return earn
    else:
        return money(earn, my_list[idx + 1:])

for i in range(T):
    print(f'#{i+1} {money(0, datum[i])}')