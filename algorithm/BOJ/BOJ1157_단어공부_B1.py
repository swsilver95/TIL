words = input()

cnt = [0] * 123

for w in words:
    tmp = ord(w.lower())
    cnt[tmp] += 1

freq = max(cnt)

if cnt.count(freq) > 1:
    print('?')
else:
    print(chr(cnt.index(freq)).upper())