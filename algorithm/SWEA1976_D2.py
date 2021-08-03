T = int(input())
for idx in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    print(f'#{idx + 1}', end=' ')
    if m1 + m2 >= 60:
        h = h1 + h2 + 1
        m = m1 + m2 - 60
        if h % 12 != 0:
            print(h % 12, m)
        else:
            print(12, m)
    else:
        if (h1 + h2) % 12 != 0:
            print((h1 + h2) % 12, m1 + m2)
        else:
            print(12, m1 + m2)
