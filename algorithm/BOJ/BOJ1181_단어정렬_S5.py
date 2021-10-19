import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
words = defaultdict(list)

for _ in range(N):
    word = input().rstrip()
    words[len(word)].append(word)


before = ''
for i in range(1, 51):
    if words[i]:
        words[i].sort()
        for j in words[i]:
            if j != before:
                print(j)
                before = j