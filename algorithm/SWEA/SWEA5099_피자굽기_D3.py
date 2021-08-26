import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    cheeze = list(enumerate(tmp, start=1))      # 0. 피자 번호를 나중에 알기 편하게 enumerate 사용
    q = []  # 화덕
    while len(q) < N:                           # 1. 화덕에 피자를 N개만큼 넣는 과정
        q.append(list(cheeze.pop(0)))

    i = 0
    while len(q) > 1:                           # 2. 피자를 화덕에 넣고 돌리는 과정
        q[i][1] //= 2                           # 2-1. i번째 인덱스의 피자에 남아있는 치즈를 절반으로 줄임
        if q[i][1] == 0:                        # 3. 치즈가 모두 녹아 없어졌을 때,
            if len(cheeze) != 0:                # 3-1. 아직 화덕에 넣을 수 있는 피자가 있다면
                q[i] = list(cheeze.pop(0))      # => 화덕에 추가
            else:                               # 3-2. 화덕에 넣을 수 있는 피자가 남아있지 않다면
                q.pop(i)                        # => 화덕에서 피자를 제거
                N -= 1                          # 3-3. 화덕에서 피자를 1개 제거했으므로 화덕의 크기를 1만큼 줄여줌
                i -= 1                          # 3-4. 마찬가지로 확인 중인 피자 번호도 i만큼 줄어줌
        i += 1                                  # 4. 다음 번 피자의 치즈를 알아보기 위해 인덱스 1만큼 증가
        if i >= N:                              # 4-1. 만약 i가 N 이상이 되어 화덕의 범위를 벗어난다면
            i -= N                              # 4-2. 다시 N만큼 빼줘서 처음부터 확인한다.

    print('#{} {}'.format(tc, q[0][0]))