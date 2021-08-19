import sys

sys.stdin = open('input.txt')

for idx in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))

    i = 0
    while i <= n:
        max_box = max(boxes)                            # 배열에서 최대값을 탐색
        max_box_idx = boxes.index(max_box)              # 최댓값이 발생하는 인덱스 저장
        min_box = min(boxes)                            # 배열에서 최소값을 탐색
        min_box_idx = boxes.index(min_box)              # 최댓값이 발생하는 인덱스 저장

        if max_box - min_box <= 1:                      # 덤프 횟수를 채우기 전에 끝날 경우
            print(max_box - min_box)                    # 그 때의 차이를 출력하고 break
            break

        boxes[max_box_idx] -= 1                         # 최댓값을 1 줄여주고
        boxes[min_box_idx] += 1                         # 최솟값을 1 늘여주고
        i += 1                                          # i에 1을 추가해서 while 반복

    print('#{} {}'.format(idx, max_box - min_box))