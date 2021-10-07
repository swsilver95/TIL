sounds = list(map(int, input().split()))

cnt_as = 0
cnt_dc = 0
for i in range(1, len(sounds)):
    if sounds[i - 1] == sounds[i] - 1:
        cnt_as += 1
    elif sounds[i - 1] == sounds[i] + 1:
        cnt_dc += 1

if cnt_as == 7:
    print('ascending')
elif cnt_dc == 7:
    print('descending')
else:
    print('mixed')