N = int(input())

paper = [[0] * 1001 for _ in range(1001)]
for p in range(1, N + 1):
    x, y, width, height = map(int, input().split())
    for i in range(width):
        for j in range(height):
            paper[x+i][y+j] = p


for p in range(1, N + 1):
    tmp = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == p:
                tmp += 1
    print(tmp)


