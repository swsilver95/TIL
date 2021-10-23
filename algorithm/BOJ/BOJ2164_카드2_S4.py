from collections import deque

N = int(input())
numbers = deque(list(range(1, N + 1)))

while len(numbers) > 1:
    numbers.popleft()
    if len(numbers) == 1:
        print(numbers[0])
        break
    a = numbers.popleft()
    numbers.append(a)

if N == 1:
    print(1)