num = (0, 0)
cnt = 0
for i in range(9):
    cnt += 1
    tmp = int(input())
    if num[0] < tmp:
        num = (tmp, cnt)

print(num[0])
print(num[1])