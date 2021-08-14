T = int(input())

for tc in range(1, T + 1):

    data = [list(map(str, input())) for _ in range(5)]
    print('#{}'.format(tc), end=' ')
    for j in range(15):
        for i in range(15):
            try:
                print(data[i][j], end='')
            except:
                pass
    print()