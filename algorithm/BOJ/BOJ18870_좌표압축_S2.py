from collections import defaultdict

N = int(input())
numbers = list(map(int, input().split()))

new_numbers = list(set(numbers))
my_dict = defaultdict(int)

new_numbers.sort()

for i in range(len(new_numbers)):
    my_dict[new_numbers[i]] = i


for number in numbers:
    print(my_dict[number], end=' ')

