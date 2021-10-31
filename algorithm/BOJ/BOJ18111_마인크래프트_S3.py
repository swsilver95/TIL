N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]


def stabilize(height, block_cnt):
    result = 0
    for row in range(N):
        for col in range(M):
            if ground[row][col] < height:
                block_cnt -= height - ground[row][col]
                result += height - ground[row][col]
            elif ground[row][col] > height:
                block_cnt += ground[row][col] - height
                result += 2 * (ground[row][col] - height)
            else:
                pass

    if block_cnt < 0:
        return -1
    else:
        return result


h = 0
answer = [1e9, 0]
while True:
    tmp = stabilize(h, B)
    if tmp != -1:
        if answer[0] >= tmp:
            answer[0] = tmp
            answer[1] = h
    else:
        break
    h += 1

print(*answer)