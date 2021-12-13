from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        cloth, cloth_type = input().split()
        clothes[cloth_type] += 1

    answer = 1
    for val in clothes.values():
        answer *= val + 1

    print(answer - 1)
