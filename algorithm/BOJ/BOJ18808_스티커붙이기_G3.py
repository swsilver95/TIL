def rotation(arr):
    row = len(arr)
    col = len(arr[0])
    rot_arr = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            rot_arr[j][row-1-i] = arr[i][j]
    return rot_arr

def check_position(slot, stik):
    global N
    global M
    row = len(stik)
    col = len(stik[0])

    if row > N or col > M:
        return 0

    for i in range(N-row+1):
        for j in range(M-col+1):
            tmp = 0
            for x in range(row):
                for y in range(col):
                    if slot[i+x][j+y] + stik[x][y] == 2:
                        tmp += 1
                        break

            if tmp == 0:
                for x in range(row):
                    for y in range(col):
                        slot[i+x][j+y] += stik[x][y]
                return slot
    return 0




N, M, K = map(int, input().split())

notebook = [[0] * M for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    for cnt in range(4):
        check = check_position(notebook, sticker)
        if check == 0:
            if cnt < 3:
                sticker = rotation(sticker)
                continue
            else:
                break
        else:
            notebook = check
            break

print(sum(sum(notebook, [])))