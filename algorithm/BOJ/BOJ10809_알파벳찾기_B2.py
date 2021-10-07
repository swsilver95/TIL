word = input()
cnt = [[] for _ in range(26)]

for i in range(len(word)):
    idx = ord(word[i]) - 97
    cnt[idx].append(i)


for c in cnt:
    if not c:
        print(-1, end=' ')
    else:
        print(c[0], end=' ')
