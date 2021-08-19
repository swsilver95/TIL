import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
                                                                # 완전 탐색
    results = []                                                # 구간합 값을 모두 추가해 줄 배열
    for i in range(N - M + 1):                                  # index를 초과하지 않는 범위 고려
        tmp = 0                                                 # 구간합을 넣어줄 임시 변수
        for j in range(i, i + M):                               # 구간 합계를 구하기 위한 반복문
            tmp += numbers[j]
        results.append(tmp)                                     # 배열에 추가

    print('#{} {}'.format(idx, max(results) - min(results)))