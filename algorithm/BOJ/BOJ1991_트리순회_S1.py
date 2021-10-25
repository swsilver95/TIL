from collections import defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(N):
    parent, left, right = map(str, input().split())
    graph[parent].append(left)
    graph[parent].append(right)


def vlr(node):
    if node != '.':
        print(node, end='')
        vlr(graph[node][0])
        vlr(graph[node][1])


def lvr(node):
    if node != '.':
        lvr(graph[node][0])
        print(node, end='')
        lvr(graph[node][1])


def lrv(node):
    if node != '.':
        lrv(graph[node][0])
        lrv(graph[node][1])
        print(node, end='')


vlr('A')
print()
lvr('A')
print()
lrv('A')
