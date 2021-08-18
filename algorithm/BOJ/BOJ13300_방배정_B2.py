N, K = map(int, input().split())

students = [[0] * 7 for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

rooms = 0
for i in range(2):
    for j in range(7):
        if students[i][j] % K == 0:
            rooms += students[i][j] // K
        else:
            rooms += students[i][j] // K + 1
print(rooms)