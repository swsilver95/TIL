N, K = map(int, input().split())


numbers = list(range(1, N + 1))

i = 0
answer = '<'
while numbers:
    i += K - 1
    i %= len(numbers)
    if len(numbers) == 1:
        answer += str(numbers.pop(i))
    else:
        answer += str(numbers.pop(i)) + ', '

answer += '>'
print(answer)
