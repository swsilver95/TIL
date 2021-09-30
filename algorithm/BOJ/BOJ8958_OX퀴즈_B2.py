T = int(input())


for _ in range(T):
    tmp = input()
    answer = 0
    cnt = 0
    for i in tmp:
        if i == 'O':
            cnt += 1
            answer += cnt
        if i == 'X':
            cnt = 0

    print(answer)