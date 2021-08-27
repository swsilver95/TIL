def lvr(node: int):                                 # 3. 중위 순회 함수(lvr)
    if node:                                        # 3-1. 유효한 노드에 대해서(0번이 아닌 노드에 대해)
        lvr(left[node])                             # 3-2. 왼쪽 노드를 먼저 재귀탐색하고
        print(words[node], end='')                  # 3-3. 현재 노드 번호와 매칭되는 문자열을 출력하고
        lvr(right[node])                            # 3-4. 오른쪽 노드를 재귀탐색한다.


for tc in range(1, 11):
    N = int(input())
    words = [0] * (N + 1)                           # 0. 정점 번호와 문자를 1:1 대응시킬 리스트
    left = [0] * (N + 1)                            # 0. 인덱스가 부모 노드, 값은 왼쪽 자식 노드
    right = [0] * (N + 1)                           # 0. 인덱스가 부모 노드, 값은 오른쪽 자식 노드

    for _ in range(N):                              # 1. 데이터를 받는 과정. N 줄을 읽어온다
        tmp = list(map(str, input().split()))       # 1-1. 알파벳이 섞여있으므로, str 형태로 저장
        try:                                        # 2. try-except 구문 활용. 자식 노드가 없을 수도 있으므로,
            for i in range(4):                      # 2-1. 인덱스 범위를 0~3까지 순회하면서
                words[int(tmp[0])] = tmp[1]         # => 노드 번호와 문자를 매칭시켜주고,
                left[int(tmp[0])] = int(tmp[2])     # => 왼쪽 자식 노드가 있다면 매칭시켜주고,
                right[int(tmp[0])] = int(tmp[3])    # => 오른쪽 자식 노드가 있다면 매칭시켜준다.
        except IndexError:                          # 2-2. 만약 왼쪽 자식 노드 혹은 오른쪽 자식 노드가 없다면, 예외처리하고 다음으로 넘어감
            continue

    print('#{}'.format(tc), end=' ')                # 4. 테스트케이스 번호를 출력하고 공백 문자를 넣은 뒤
    lvr(1)                                          # 4-1. 중위순회 시작
    print()                                         # 4-2. 한 번의 테스트케이스가 끝나면 다음 테스트케이스를 위해 개행문자 삽입
