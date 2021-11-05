N = int(input())

i = 0
numbers = set()
numbers.add(N)

while 1 not in numbers:
    i += 1
    tmp_numbers = set()
    for number in numbers:
        if number % 3 == 0:
            tmp_numbers.add(number // 3)
        if number % 2 == 0:
            tmp_numbers.add(number // 2)
        if number - 1 > 0:
            tmp_numbers.add(number - 1)

    numbers = tmp_numbers

print(i)
