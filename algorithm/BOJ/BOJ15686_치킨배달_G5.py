from itertools import combinations
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
houses = []
chicken_shop = []


def check_position(city):
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append([i, j])
            elif city[i][j] == 2:
                chicken_shop.append([i, j])


def find_chicken_distance(houses, chickens):
    min_total = 999999
    # 모든 케이스에 대해서
    for chicken in chickens:
        total = 0
        # 하나의 케이스에서 도시의 치킨 거리의 총합
        for house in houses:
            chicken_distance = 101
            # 하나의 집에 대해서 치킨집과의 거리를 구해서 tmp에 저장
            for i in range(M):
                tmp = abs(house[0] - chicken[i][0]) + abs(house[1] - chicken[i][1])
                if chicken_distance > tmp:
                    chicken_distance = tmp
            total += chicken_distance
        # 하나의 케이스가 끝나면, 해당 케이스와 다른 케이스의 치킨 거리를 비교
        if min_total > total:
            min_total = total

    return min_total


check_position(city)
chicken_shop_selections = list(combinations(chicken_shop, M))
# print(houses)
# print(chicken_shop)
# print(M)
# print(chicken_shop_selections)
print(find_chicken_distance(houses, chicken_shop_selections))