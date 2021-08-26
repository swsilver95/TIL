import sys
sys.stdin = open('input.txt')

T = int(input())


def permutation(idx):
    global temp, min_num            # temp : 배열 합을 저장한 임시 변수

    if min_num < temp:              # 현재 min_num보다 temp가 더 크면
        return                      # 더 확인할 필요가 없으므로 return

    if idx == N:                    # 모든 원소에 대해 선택한 과정을 거친 뒤에
        if min_num > temp:          # min_num보다 temp가 더 작으면
            min_num = temp          # min_num을 교체
        return

    for i in range(N):
        if check[i] == 0:           # 해당 원소를 아직 사용하지 않았다면
            temp += arr[idx][i]     # 선택한 원소를 temp에 합한다.
            check[i] = 1            # 해당 원소를 사용했다는 뜻
            permutation(idx + 1)    # 다음 자리를 확인
            temp -= arr[idx][i]     # 다음엔 제외할 것이므로 temp에서 다시 뺀다
            check[i] = 0            # 다음 반복문을 위해 check 초기화


for tc in range(1, T + 1):
    min_num = 2147483647
    temp = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    permutation(0)
    print('#{} {}'.format(tc, min_num))
