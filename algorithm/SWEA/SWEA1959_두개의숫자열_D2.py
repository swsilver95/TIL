T = int(input())

for idx in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(f'#{idx + 1}', end=' ')

    result = []
    if len(A) > len(B):
        for i in range(len(A) - len(B) + 1):
            tmp = 0
            for j in range(len(B)):
                tmp += A[i+j] * B[j]
            result.append(tmp)
        print(max(result))

    else:
        for i in range(len(B) - len(A) + 1):
            tmp = 0
            for j in range(len(A)):
                tmp += A[j] * B[i+j]
            result.append(tmp)
        print(max(result))