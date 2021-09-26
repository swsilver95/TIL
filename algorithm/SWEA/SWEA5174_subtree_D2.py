import sys
sys.stdin = open('input.txt')

T = int(input())


def vlr(node):              # 1. 전위 순회 함수 구성(뭐든 상관 없음)
    global cnt              # 1.1. 확인한 노드의 개수
    if node:                # 1.2. 전위 순회
        cnt += 1            # 1.3. 확인하면 카운트 + 1
        vlr(tree[node][0])
        vlr(tree[node][1])


for tc in range(1, T + 1):
    E, N = map(int, input().split())                    # 2. 간선과 subtree의 root 노드 번호를 받고
    edges = list(map(int, input().rstrip().split()))    # 2.1. 간선들을 받아와서
    tree = [[0, 0, 0] for _ in range(E + 2)]
    for i in range(E):                                  # 2.2. 트리에 입력
        parent, child = edges[i*2], edges[i*2+1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    cnt = 0                             # 3. 확인한 노드 개수 변수를 0으로 초기화
    vlr(N)                              # 4. 순회하고 돌아옴
    print('#{} {}'.format(tc, cnt))     # 5. cnt가 곧 노드의 개수이므로 출력
