import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())         # N은 곡 수 / S는 시작 볼륨 / M은 최대 볼륨
volumes = [0] + list(map(int, input().split()))


can_play = [[False for _ in range(M + 1)] for _ in range(N + 1)]
can_play[0][S] = True


def last_volume(N, M):
    for num in range(1, N + 1):
        cnt = 0
        for vol in range(M + 1):
            if can_play[num - 1][vol]:
                if 0 <= vol - volumes[num] <= M:
                    can_play[num][vol - volumes[num]] = True
                    cnt += 1

                if 0 <= vol + volumes[num] <= M:
                    can_play[num][vol + volumes[num]] = True
                    cnt += 1
        if cnt == 0:
            return -1
    for i in range(M, -1, -1):
        if can_play[N][i]:
            return i


print(last_volume(N, M))


