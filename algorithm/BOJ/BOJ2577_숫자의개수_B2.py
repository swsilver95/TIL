A = int(input())
B = int(input())
C = int(input())

numbers = str(A * B * C)
cnt = [0] * 10

for number in numbers:
    cnt[int(number)] += 1

for i in range(10):
    print(cnt[i])