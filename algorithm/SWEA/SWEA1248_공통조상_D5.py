import sys
sys.stdin = open('input.txt')

T = int(input())


def side(node):
    global cnt, node_cnt
    left_node = tree[node][0]
    right_node = tree[node][1]

    cnt = 0
    node_cnt = 0
    left_cnt = vlr(left_node)
    if cnt == 2:
        L = True
    else:
        L = False
    cnt = 0
    node_cnt = 0
    right_cnt = vlr(right_node)
    if cnt == 2:
        R = True
    else:
        R = False

    if L and not R:
        available.append([left_node, left_cnt])
        side(left_node)
    elif R and not L:
        available.append([right_node, right_cnt])
        side(right_node)
    else:
        return


def vlr(node):
    global cnt, node_cnt
    if node == n1:
        cnt += 1
    if node == n2:
        cnt += 1
    if node:
        node_cnt += 1
        vlr(tree[node][0])
        vlr(tree[node][1])

    return node_cnt


for tc in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    tree = [[0, 0, 0] for _ in range(V + 1)]
    tmp = list(map(int, input().split()))

    for i in range(E):
        parent, child = tmp[i*2], tmp[i*2 + 1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent
    node_cnt = 0
    cnt = 0
    available = []
    side(1)
    if not available:
        node_cnt = 0
        cnt = vlr(1)
        print('#{} {} {}'.format(tc, 1, cnt))
    else:
        print('#{} {} {}'.format(tc, available[-1][0], available[-1][1]))