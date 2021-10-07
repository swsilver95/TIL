n = int(input())
data = []
for _ in range(n):
    A, B = list(map(int, input().split()))
    data.append((A, B))

data.sort()
cnt = 1
end = data[0][1]
for i in range(1, len(data)):
    if end > data[i][1]:
        end = data[i][1]
    elif end <= data[i][0]:
        cnt += 1
        end = data[i][1]

print(cnt)

