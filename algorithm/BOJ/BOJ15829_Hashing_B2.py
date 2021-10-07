L = int(input())
words = input()

answer = 0
for i in range(L):
    answer += (ord(words[i]) - 96) * (31 ** i)

print(answer % 1234567891)