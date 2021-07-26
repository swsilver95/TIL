import itertools

N, M = map(int, input().split())

numbers = list(range(1, N+1))
num_lists = list(itertools.combinations(numbers, M))
# print(num_list)

for num_list in num_lists:
    for i in num_list:
        print(i, end=' ')
    print()