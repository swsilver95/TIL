N = int(input())
numbers = list(map(int, input().split()))

up_cnt = 1
down_cnt = 1
max_len = 0
for i in range(1, N):
    if numbers[i - 1] <= numbers[i]:        # 숫자가 연속해서 커지는 경우
        up_cnt += 1
        max_len = max(max_len, up_cnt)
    else:
        up_cnt = 1

for i in range(1, N):                       # 숫자가 연속해서 작아지는 경우
    if numbers[i - 1] >= numbers[i]:
        down_cnt += 1
        max_len = max(max_len, down_cnt)
    else:
        down_cnt = 1

if N == 1:
    print(1)
else:
    print(max_len)