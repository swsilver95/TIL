import math

A, B, V = map(int, input().split())

h = A - B
answer = math.ceil((V - A) / h) + 1

print(answer)
