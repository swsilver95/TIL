import sys
input = sys.stdin.readline
N = int(input())

people = []
for _ in range(N):
    age, name = map(str, input().rstrip().split())
    people.append((int(age), name))

people.sort(key=lambda x: x[0])

for person in people:
    print(*person)

