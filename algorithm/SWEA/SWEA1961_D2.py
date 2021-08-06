T = int(input())

def rotate(matrix, r=90):
    n = len(matrix)
    my_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            my_matrix[j][n-1-i] = matrix[i][j]

    if r > 90:
        return rotate(my_matrix, r - 90)
    elif r <= 90:
        return my_matrix


for idx in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    m90 = rotate(data)
    m180 = rotate(data, 180)
    m270 = rotate(data, 270)

    print(f'#{idx+1}')
    for i in range(N):
        print(''.join(map(str, m90[i])), end=' ')
        print(''.join(map(str, m180[i])), end=' ')
        print(''.join(map(str, m270[i])))