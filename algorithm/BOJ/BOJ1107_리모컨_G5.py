from itertools import product
import sys

N = int(input())
M = int(input())
channels = set(map(int, input().split()))

if N == 100:
    print(0)
    sys.exit(0)

if M == 10:
    print(abs(N - 100))
    sys.exit(0)


available = set(range(0, 10)) - channels
numbers = []
for a in range(1, len(str(N)) + 2):
    numbers += list(int(''.join(map(str, i))) for i in product(available, repeat=a))

answer = abs(N - 100)
while numbers:
    k = numbers.pop()
    result = len(str(k)) + abs(N - k)

    if answer > result:
        answer = result


print(answer)

