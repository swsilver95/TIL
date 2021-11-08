N, M = map(int, input().split())

hear = set()
see = set()

for _ in range(N):
    hear.add(input())

for _ in range(M):
    see.add(input())


answer = hear & see
answer = list(answer)
answer.sort()

print(len(answer))
for name in answer:
    print(name)
