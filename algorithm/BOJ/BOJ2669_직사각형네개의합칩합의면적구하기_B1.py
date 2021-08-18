square = [[0] * 101 for _ in range(101)]        # 101 * 101의 빈 배열 생성
for _ in range(4):                              # 사각형이 4개이므로 range(4)
    x1, y1, x2, y2 = map(int, input().split())  # 각 좌표를 map을 이용해서 받고
    for i in range(x2-x1):                      # 점과 면적의 차이에 유의하면서
        for j in range(y2-y1):                  # range의 범위를 두 좌표의 차이로 둠
            square[x1+i][y1+j] += 1             # 사각형을 직접 그려가면서 1씩 더해담

cnt = 0
for i in range(101):
    for j in range(101):
        if square[i][j] != 0:                   # 최종 결과를 조회하면서
            cnt += 1                            # 사각형이 한개라도 겹친 곳은 count

print(cnt)