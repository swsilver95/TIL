T = int(input())

def even_minus(n):
    if int(n) % 2 != 0:
        return int(n)
    else:
        return int(n) - 1

for tc in range(1, T + 1):
    N = int(input())
    moves = []
    for _ in range(N):
        moves.append(list(map(even_minus, input().split())))

    cnt = [0] * 401
    for move in moves:
        if move[0] < move[1]:
            for i in range(move[0], move[1] + 1):
                cnt[i] += 1
        else:
            for i in range(move[1], move[0] + 1):
                cnt[i] += 1

    print('#{} {}'.format(tc, max(cnt)))