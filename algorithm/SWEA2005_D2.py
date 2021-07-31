T = int(input())
for idx in range(T):
    number = int(input())
    print(f'#{idx + 1}')
    if number <= 1:
        print(1)
        continue
    pascal = []
    for _ in range(number):
        tmp = []
        for _ in range(number):
            tmp.append(0)
        pascal.append(tmp)
    pascal[0][0] = 1
    pascal[1][0] = 1
    pascal[1][1] = 1
    if number == 2:
        for m in range(number):
            for n in range(number):
                if pascal[m][n] != 0:
                    print(pascal[m][n], end=' ')
            print()
    
    else:
        for i in range(2, number):
            for j in range(number):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        for k in range(number):
            for l in range(number):
                if pascal[k][l] != 0:
                    print(pascal[k][l], end=' ')
            print()