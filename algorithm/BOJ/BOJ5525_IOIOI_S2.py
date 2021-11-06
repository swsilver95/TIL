N = int(input())
M = int(input())
S = input()

my_I = ['I'] * (N + 1)
pattern = 'O'.join(my_I)

cnt = 0
i = 0
while i < M:
    # print(i)
    if S[i] == 'I':
        j = 1
        while True:
            # print(j)
            if i + j >= M:
                i += j
                break

            if j % 2:
                if S[i + j] != 'O':
                    i += j
                    break
            else:
                if S[i + j] != 'I':
                    i += j
                    break
            j += 1

        if (j - 1) // 2 >= N:
            cnt += (j - 1) // 2 - N + 1
    else:
        i += 1
        # print(i)

print(cnt)