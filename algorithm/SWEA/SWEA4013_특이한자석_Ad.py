T = int(input())


# n번째 기어를 r 방향으로 돌리는 함수
def rotate(n, r):
    # 시계 방향이면,
    # n-1번째 인덱스 값을 팝해서 앞에 더하고
    if r == 1:
        a = gears[n - 1].pop()
        gears[n - 1].insert(0, a)
    # 반시계 방향이면,
    # n-1번째 인덱스 값의 첫번째 값을 빼서 뒤에 더함
    else:
        a = gears[n - 1].pop(0)
        gears[n - 1].append(a)


# n번째 기어의 왼쪽을 어떻게 돌릴지 정하는 함수
def run_left(n, r):
    # 첫 번째 기어라면 왼쪽이 없으므로 리턴
    if n <= 1:
        return
    # 두 번째 이상의 기어라면,
    else:
        # 만약 n번째 기어와 n-1번째 기어가 붙어있는 곳의 자극이 다를 때,
        if gears[n - 1][-2] != gears[n - 2][2]:
            # n-1번째 기어가 첫 번째 기어이면
            # 첫 번째 기어를 회전시키고 종료
            if n - 2 == 0:
                rotate(n - 1, -r)
                return
            # n-1번째 기어가 첫 번째 기어가 아니라면
            # n-2번째 기어와 n-1번째 기어를 비교
            else:
                # n-2번째 기어와 n-1번째 기어가 붙어있는 곳의 극도 다르면,
                # 또 회전해야 하므로 왼쪽으로 한 칸 이동해서 재귀 호출, 방향은 -r방향
                if gears[n - 2][-2] != gears[n - 3][2]:
                    run_left(n - 1, -r)
                rotate(n - 1, -r)
        else:
            return


def run_right(n, r):
    if n >= 4:
        return
    else:
        if gears[n][-2] != gears[n - 1][2]:
            if n + 1 == 4:
                rotate(n + 1, -r)
                return
            else:
                if gears[n + 1][-2] != gears[n][2]:
                    run_right(n + 1, -r)
                rotate(n + 1, -r)
        else:
            return


for tc in range(1, T + 1):
    gears = []
    K = int(input())
    for _ in range(4):
        gears.append(list(map(int, input().rstrip().split())))

    for _ in range(K):
        n, r = map(int, input().rstrip().split())
        run_left(n, r)
        run_right(n, r)
        rotate(n, r)
        # print(gears)

    point = 0
    for i in range(4):
        if i == 0:
            if gears[i][0] == 1:
                point += 1
        if i == 1:
            if gears[i][0] == 1:
                point += 2
        if i == 2:
            if gears[i][0] == 1:
                point += 4
        if i == 3:
            if gears[i][0] == 1:
                point += 8

    print('#{} {}'.format(tc, point))
