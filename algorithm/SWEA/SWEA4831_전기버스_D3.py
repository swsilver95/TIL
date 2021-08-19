import sys

sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T + 1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    stops = [0] * (N + 1)                                               # 충전소 위치를 표시할 리스트
    for charge in charges:                                              # 충전소가 있는 곳을 1로 지정
        stops[charge] = 1
    p = 0                                                               # 현재 위치
    s = K
    cnt = 0                                                             # 충전 횟수
    while p <= N:
        if p + s >= N:                                                  # 만약 p에서 s만큼 갔을 때 종점에 도달할 수 있다면
            print('#{} {}'.format(idx, cnt))                            # cnt를 출력하고 break
            break

        if stops[p + s] == 1:                                           # 만약 p에서 s만큼 이동한 곳에 충전소가 있다면
            p += s                                                      # p의 위치를 해당 충전소로 변경
            cnt += 1
            s = K                                                       # 다시 s를 최대치인 K만큼으로 변경
        else:                                                           # 만약 s만큼 앞에 충전소가 없다면
            s -= 1                                                      # s보다 한 칸 앞을 찾아보도록 유도
            if s == 0:                                                  # 만약 s가 0이 되면
                print('#{} {}'.format(idx, 0))                          # 불가능을 출력하고 break
                break
