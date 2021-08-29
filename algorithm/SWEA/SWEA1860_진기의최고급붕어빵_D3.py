T = int(input())


def can_give(numbers):                              # 1. 붕어빵을 줄 수 있는지 여부를 확인하는 함수
    global M, K                                     # 2. 글로벌 변수 지정
    bread_num = 0                                   # 2-1. 빵 개수를 저장할 변수
    cnt = 0                                         # 2-2. 먼저 와서 빵을 받아간 사람의 수

    while numbers:                                  # 3. 모든 사람이 붕어빵을 다 가져갈 때까지,
        # 먼저 온 사람(빠른 시간)부터 확인하기 위해 아까 정렬함
        person = numbers.pop()                      # 3-1. 가장 먼저 도착한 사람부터 순서대로 pop()
        cnt += 1                                    # 3-2. 붕어빵을 하나 가져갔으므로 cnt에 +1
        bread_num = (person // M) * K - cnt        # 3-3. 잔여 붕어빵 개수
        if bread_num < 0:                           # 4. 잔여 붕어빵 개수가 0보다 작아질 순 없으므로
            return 'Impossible'                     # 4-1. 해당 경우가 생기면 불가능을 출력
    return 'Possible'                               # 5. 무사히 while문을 돌았다면, 가능을 출력


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())             # 0. M초마다 K개의 붕어빵을 만들어냄
    people = list(map(int, input().split()))        # 0. 사람이 언제 오는지 리스트로 받음
    people.sort(reverse=True)                       # 0. pop()을 활용하기 위해서 역순 정렬 시도
    print('#{} {}'.format(tc, can_give(people)))
