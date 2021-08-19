import sys
sys.stdin = open('input.txt')

T = int(input())

def paper_paste(N):                                         # 종이 개수를 반환하는 함수
    n = N // 10                                             # n은 N을 10으로 나눈 몫
    result = [0, 1, 3]
    if n <= 2:                                              # 인덱스 에러를 방지하기 위해 n이 2 이하인 경우는 미리 계산한 결과를 출력
        return result[n]

    for i in range(3, n + 1):                               # [i-1]번째 경우의 개수 + 2*[i-2]번째 경우의 개수를 발견
        result.append(result[i - 1] + 2*result[i - 2])      # 점화식을 이용해서 결과에 추가하는 방식

    return result[-1]                                       # 결과 배열의 끝값을 출력


for tc in range(1, T + 1):
    N = int(input())

    print('#{} {}'.format(tc, paper_paste(N)))
