from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))
idx = list(range(N))
cases = combinations(idx, 3)

answer = 0
for case in cases:
    a, b, c = case
    tmp = cards[a] + cards[b] + cards[c]
    if answer < tmp <= M:
        answer = tmp

print(answer)
