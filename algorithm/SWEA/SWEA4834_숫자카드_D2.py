import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T + 1):
    n = int(input())
    numbers = input()
    cnt = [0] * 10                                      # 0부터 1까지의 개수를 담을 리스트
    for number in numbers:                              # 각 숫자별 카운팅
        cnt[int(number)] += 1
    max_cnt = max(cnt)                                  # 최대 등장 횟수를 max_cnt에 저장

    for i in range(9, -1, -1):                          # 동일한 횟수이면 큰 숫자를 출력해야 하므로 뒤에서부터 탐색
        if cnt[i] == max_cnt:                           # 등장 횟수가 max_cnt와 같다면
            max_num = i                                 # 최빈 숫자를 지정
            break
    print('#{} {} {}'.format(idx, max_num, max_cnt))