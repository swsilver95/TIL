import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())             # 0. N: 노드의 개수, M: 리프노드의 개수, L: 노드번호
    nodes = [0] * (N + 1)                           # 0. 각 노드가 가지고 있는 값을 0으로 초기화
    for _ in range(M):                              # 1. M개의 리프노드에 값을 입력
        leaf, value = map(int, input().split())
        nodes[leaf] = value

    for i in range(N, 0, -1):                       # 2. 노드를 역순으로 순회하면서
        parent = i // 2                             # 2.1. 부모노드는 노드번호를 2로 나눈 몫이고,
        nodes[parent] += nodes[i]                   # 2.2. 각 노드의 부모노드에 자기 자신의 값을 더해주면서 트리를 완성

    print('#{} {}'.format(tc, nodes[L]))