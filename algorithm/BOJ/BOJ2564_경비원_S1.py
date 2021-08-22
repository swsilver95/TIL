width, height = map(int, input().split())
n = int(input())
'''
북쪽 1
남쪽 2
서쪽 3
동쪽 4
'''
shops = []
for _ in range(n):
    shops.append(list(map(int, input().split())))
p = list(map(int, input().split()))

total = 0
if p[0] == 1:
    for shop in shops:
        if shop[0] == 1:    # 북
            total += abs(shop[1] - p[1])
        elif shop[0] == 2:  # 남
            total += min(p[1] + height + shop[1], width - p[1] + height + width - shop[1])
        elif shop[0] == 3:  # 서
            total += shop[1] + p[1]
        elif shop[0] == 4:  # 동
            total += width - p[1] + shop[1]
elif p[0] == 2:
    for shop in shops:
        if shop[0] == 1:
            total += min(p[1] + height + shop[1], width - p[1] + height + width - shop[1])
        elif shop[0] == 2:
            total += abs(shop[1] - p[1])
        elif shop[0] == 3:
            total += p[1] + height - shop[1]
        elif shop[0] == 4:
            total += width - p[1] + height - shop[1]
elif p[0] == 3:
    for shop in shops:
        if shop[0] == 1:
            total += p[1] + shop[1]
        elif shop[0] == 2:
            total += height - p[1] + shop[1]
        elif shop[0] == 3:
            total += abs(shop[1] - p[1])
        elif shop[0] == 4:
            total += min(p[1] + width + shop[1], height - p[1] + width + height - shop[1])
elif p[0] == 4:
    for shop in shops:
        if shop[0] == 1:
            total += p[1] + width - shop[1]
        elif shop[0] == 2:
            total += height - p[1] + width - shop[1]
        elif shop[0] == 3:
            total += min(p[1] + width + shop[1], height - p[1] + width + height - shop[1])
        elif shop[0] == 4:
            total += abs(shop[1] - p[1])

print(total)

