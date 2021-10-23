import math
N, K = map(int, input().split())

a = math.factorial(N) // (math.factorial(N - K) * math.factorial(K))

print(a)