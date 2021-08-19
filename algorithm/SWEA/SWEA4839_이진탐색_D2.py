import sys

sys.stdin = open('input.txt')

def searchCount(number, target):                    # 이진탐색 정의
    left = 1
    right = number
    cnt = 0

    while left <= right:                            
        mid = int((left + right) / 2)               # 중앙값은 문제에 적힌 그대로 계산
        if mid == target:
            return cnt
        elif mid < target:                          # 만약 중앙값이 찾고자 하는 값보다 작다면
            left = mid                              # 왼쪽 한계값을 중앙값으로 옮겨주고
            cnt += 1                                # 찾는 횟수 1회 증가
        else:
            right = mid
            cnt += 1
    return cnt                                      # 최종적으로는 탐색 횟수 반환


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    Pa_page = searchCount(P, Pa)
    Pb_page = searchCount(P, Pb)
    if Pa_page > Pb_page:                           # a가 찾는데 더 오래 걸렸다면, B가 승리
        print('#{} {}'.format(tc, 'B'))
    elif Pa_page < Pb_page:                         # b가 찾는데 더 오래 걸렸다면, A가 승리
        print('#{} {}'.format(tc, 'A'))
    else:                                           # 이외의 경우에는 무승부
        print('#{} {}'.format(tc, 0))