# from pprint import pprint
T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    print(f'#{idx + 1}', end=' ')
    data = [[0 for _ in range(N+2)]]
    for _ in range(N):
        data.append([0] + list(map(int, input().split())) + [0])
    data.append([0 for _ in range(N+2)])
    # print(data)
    slot_hor = []
    for i in range(N+2):
        for j in range(N+2):
            if data[i][j] == 1 and data[i][j-1] == 0:
                cnt = 1
            elif data[i][j] == 1 and data[i][j-1] == 1:
                cnt += 1
            elif data[i][j] == 0 and data[i][j-1] == 1:
                slot_hor.append(cnt)
                cnt = 0
    
    slot_ver = []
    for j in range(N+2):
        for i in range(N+2):
            if data[i][j] == 1 and data[i-1][j] == 0:
                cnt = 1
            elif data[i][j] == 1 and data[i-1][j] == 1:
                cnt += 1
            elif data[i][j] == 0 and data[i-1][j] == 1:
                slot_ver.append(cnt)
                cnt = 0
    # print(slot_hor)
    # print(slot_ver)

    print(slot_hor.count(K) + slot_ver.count(K))
