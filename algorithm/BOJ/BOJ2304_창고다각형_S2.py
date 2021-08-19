N = int(input())

warehouse = [0 for _ in range(1001)]
for _ in range(N):
    L, H = map(int, input().split())
    warehouse[L] = H
# print(warehouse)


def warehouse_area(data):
    max_height = max(data)
    area = max_height
    max_idx = data.index(max_height)
    data_left = data[:max_idx]                  # 최대가 나타나는 곳 기준으로 왼쪽으로 슬라이싱
    data_right = data[max_idx + 1:]             # 최대가 나타나는 곳 기준으로 오른쪽으로 슬라이싱

    while True:                                 # 왼쪽에서 돌아갈 루프
        max_height_left = max(data_left)        # 왼쪽 부분에서의 최대값
        max_idx_next = data_left.index(max_height_left)        # 왼쪽 부분에서 최대가 나타나는 위치의 인덱스
        area += (max_idx - max_idx_next) * max_height_left     # 넓이 추가
        data_left = data_left[:max_idx_next]    # 왼쪽 부분 갱신
        max_idx = max_idx_next                  # 이전 인덱스에 이번 인덱스를 저장
        if len(data_left) == 0:                 # 왼쪽 부분이 모두 비었거나
            break
        elif max(data_left) == 0:               # 왼쪽 부분에 남은게 없으면
            break                               # break

    max_idx = data.index(max_height)
    while True:
        max_height_right = max(data_right)
        max_idx_next = data_right.index(max_height_right)
        area += (max_idx_next + 1) * max_height_right
        data_right = data_right[max_idx_next + 1:]
        if len(data_right) == 0:
            break
        elif max(data_right) == 0:
            break

    return area

print(warehouse_area(warehouse))