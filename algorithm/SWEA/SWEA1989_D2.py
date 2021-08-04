T = int(input())
for idx in range(T):
    print(f'#{idx + 1}', end=' ')
    word = input().rstrip()
    if word == word[::-1]:
        print(1)
    else:
        print(0)