A = int(input())
X = int(input())

numbers = [1, A % 1000000007]

i = 1
while i <= X:
    i *= 2
    tmp = (numbers[-1] ** 2) % 1000000007
    numbers.append(tmp)

X = bin(X)[2:]
answer = 1
# print(numbers)
# print(X)
for i in range(len(X)):
    if X[i] == '1':
        j = len(X) - i
        answer = (answer * numbers[j]) % 1000000007

print(answer)