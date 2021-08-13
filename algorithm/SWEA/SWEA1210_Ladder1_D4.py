# import sys

# sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    ladder = [[0] * 102]
    for _ in range(100):                            # 인덱스 초과를 고려하지 않기 위해 0으로 벽을 두름
        ladder.append([0] + list(map(int, input().split())) + [0])
    ladder.append([0] * 102)
    # print(len(ladder))

    dx = [-1, 0, 0]     # 위 왼쪽 오른쪽
    dy = [0, -1, 1]

    x = 100
    y = ladder[100].index(2)
    d = 0

    while x > 0:
        nx = x + dx[d]
        ny = y + dy[d]
        if ladder[x - 1][y] == 0:                   # 위쪽이 0이면
            x, y = nx, ny                           # 가던 방향 그대로 진행
        else:                                       # 위쪽이 1이라면,
            if d == 0:                              # 1. 진행 방향이 위쪽일 때
                for r in range(1, 3):               # 좌, 우에 1이 있는지 검색
                    tnx = x + dx[r]
                    tny = y + dy[r]
                    if ladder[tnx][tny] == 1:       # 어느 한 쪽에 1이 있으면
                        x, y = tnx, tny             # x, y좌표를 해당 방향으로 변경해주고
                        d = r                       # 방향도 해당 방향으로 변경
                        break                       # if문 break, 따라서 for else문은 실행되지 않음
                else:                               # 좌우에 1이 없다면, 올라가던대로 위로 올라감
                    x, y = nx, ny
            elif d != 0 and ladder[nx][ny] != 0:    # 2. 위로 올라가는 중이 아니면서 해당 방향 앞칸이 0이 아니라면
                x, y = nx, ny                       # 그대로 계속 진행
            else:                                   # 위로 올라가는 중이 아니면서 해당 방향 앞칸이 0이면
                x, y = x - 1, y                     # 더 이상 진행할 수 없으므로 위로 올라감
                d = 0                               # 다시 방향은 위쪽 방향으로 변경

    print('#{} {}'.format(tc, y - 1))               # 최종 지점의 y좌표 출력



