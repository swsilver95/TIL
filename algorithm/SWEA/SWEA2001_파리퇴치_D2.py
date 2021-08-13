T = int(input())
for idx in range(T):
    print(f'#{idx + 1}', end=' ')
    N, M = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    # print(data)

    result = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = []
            for k in range(M):
                fly += data[i+k][j:j+M]
                # print(fly)
                if len(result) == 0:
                    result.append(sum(fly))
                else:
                    if result[-1] <= sum(fly):
                        result.append(sum(fly))
    
    print(result[-1])