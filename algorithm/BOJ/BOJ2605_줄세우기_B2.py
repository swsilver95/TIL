N = int(input())
numbers = list(map(int, input().split()))

result = []
stack = []
for i in range(N):
    result.insert(i - numbers[i], i + 1)

print(*result)