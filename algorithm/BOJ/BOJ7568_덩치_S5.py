N = int(input())
people = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append([x, y])

for person in people:
    cnt = 1
    for i in range(N):
        if person[0] < people[i][0] and person[1] < people[i][1]:
            cnt += 1
    print(cnt, end=' ')
