width, height = map(int, input().split())
T = int(input())


def find_gap(numbers):                                      # 리스트를 받아, 인접한 두 수의 차가 가장 클 때의 차를 반환
    k = len(numbers)
    max_gap = 0
    for i in range(k - 1):
        tmp = numbers[i + 1] - numbers[i]
        max_gap = max(max_gap, tmp)
    return max_gap


square = [[0] * (width + 1) for _ in range(height + 1)]     # 점선의 개수는 사각형의 길이보다 1 길다
horizontal_cut = [0, height]                                # 가로 컷팅 인덱스 모음
vertical_cut = [0, width]                                   # 세로 컷팅 인덱스 모음
for _ in range(T):
    d, n = map(int, input().split())                        # 0: 가로 / 1: 세로
    if d == 0:
        horizontal_cut.append(n)
    else:
        vertical_cut.append(n)

horizontal_cut.sort()                                       # 인접한 두 수의 차를 구하기 위해 정렬
vertical_cut.sort()
# print(horizontal_cut, 'hor')
# print(vertical_cut, 'ver')

x = find_gap(horizontal_cut)
# print(x)
y = find_gap(vertical_cut)
# print(y)

print(x*y)