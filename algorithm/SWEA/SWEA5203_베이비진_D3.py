import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def baby_gin(cnt):
    # 1. run
    tmp = 1
    for k in range(1, 10):
        if cnt[k - 1] != 0 and cnt[k] != 0:
            tmp += 1
            if tmp >= 3:
                return True
        elif cnt[k - 1] == 0 and cnt[k] != 0:
            tmp = 1

    # 2. triplet
    for j in range(10):
        if cnt[j] >= 3:
            return True

    return False


for tc in range(1 ,T + 1):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    p1 = [0] * 10
    p2 = [0] * 10
    answer = 0
    for i in range(n):
        # 플레이어 1
        if i % 2 == 0:
            p1[numbers[i]] += 1
            if baby_gin(p1):
                answer = 1
                break
        else:
            p2[numbers[i]] += 1
            if baby_gin(p2):
                answer = 2
                break

    print('#{} {}'.format(tc, answer))