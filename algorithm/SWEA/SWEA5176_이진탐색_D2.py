import sys
sys.stdin = open('input.txt')

T = int(input())


def lvr(node):                  # 1. 중위순회 함수 구성
    if node:                    # 1.1. 노드가 0이 아니라면
        lvr(nodes[node*2])      # 1.2. 왼쪽 탐색
        order.append(node)      # 1.3. order 배열에 탐색한 순서대로 노드 번호를 추가
        lvr(nodes[node*2 + 1])  # 1.4. 오른쪽 탐색


for tc in range(1, T + 1):
    N = int(input())                            # 0. N: N번 노드까지 존재
    nodes = list(range(N + 1)) + [0] * (N + 1)  # 0. 인덱스는 노드 번호, 값도 노드 번호를 가지는 배열 초기화
    tree = [0] * (N + 1)                        # 0. 정답을 작성할 트리 초기화
    order = []                                  # 0. 탐색한 노드번호를 순서대로 넣을 배열 초기화
    lvr(1)              # 1. 중위순회

    i = 1               # 2. i를 1로 초기화하여
    for num in order:   # 2.1. order 배열에 탐색한 노드 순서대로 i를 부여
        tree[num] = i
        i += 1          # 2.1. i를 1씩 증가

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))