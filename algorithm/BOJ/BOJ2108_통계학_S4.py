N = int(input())

min_number = 4001
max_number = -4001
total = 0
numbers = []
cnt = [0] * 8001

for _ in range(N):
    n = int(input())
    if min_number > n:
        min_number = n

    if max_number < n:
        max_number = n

    cnt[n + 4000] += 1
    total += n
    numbers.append(n)


numbers.sort()
print(round(total / N))
print(numbers[N // 2])

freq = max(cnt)
nums = []
for i in range(8001):
    if cnt[i] == freq:
        nums.append(i - 4000)
if len(nums) >= 2:
    nums.sort()
    print(nums[1])
else:
    print(nums[0])
print(max_number - min_number)

