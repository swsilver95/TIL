T = int(input())

building = [[0] * 15 for _ in range(15)]
for i in range(15):
    building[0][i] = i

for height in range(1, 15):
    for ho in range(1, 15):
        building[height][ho] = sum(building[height - 1][:ho + 1])

for tc in range(T):
    k = int(input())
    n = int(input())
    print(building[k][n])
