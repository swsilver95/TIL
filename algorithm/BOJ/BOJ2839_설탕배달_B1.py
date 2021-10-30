N = int(input())

if N % 5 == 0:
    print(N // 5)

else:
    i = 0
    while N > 0 and N % 5 != 0:
        N -= 3
        i += 1
    if N < 0:
        print(-1)
    else:
        print(i + N // 5)
