import sys

T = int(sys.stdin.readline())

# x의 가장 부모 노드를 찾는 함수
def find(x):
    # 만약 자기 자신이 부모 노드라면 x를 그대로 리턴
    if parent[x] == x:
        return x
    # 그렇지 않다면 부모 노드라 적힌 곳을 찾으러 일단 위로 올라가봅시다.
    else:
        p = find(parent[x])
        # 다 찾고 돌아오면 p가 제일 마지막 부모 노드란 소리겠지요
        # x의 최상단 부모 노드를 p라고 저장해버립시다.
        parent[x] = p
        # 이제 리턴 ㄱㄱ
        return p


# x라는 친구가 포함된 곳과 y라는 친구가 포함된 곳을 합쳐주는 함수
def union(x, y):
    # 일단 x하고 y의 부모 노드가 어딘지부터 각각 알아보고요
    x, y = find(x), find(y)

    # 부모 노드가 다르다면 합쳐야 된다는 뜻이지요.
    if x != y:
        # y의 부모 노드를 x로 만들어버려서 합쳐줍시다.
        parent[y] = x
        # 각 그룹에 속해 있던 사람들 수도 합쳐주고요.
        number[x] += number[y]
    # 몇 명인지 리턴합시다.
    return number[x]


for _ in range(T):
    F = int(sys.stdin.readline())
    parent = dict()
    number = dict()
    for _ in range(F):
        p1, p2 = map(str, sys.stdin.readline().split())
        # 만약 p1이라는 친구가 parent에 없다면,
        if not parent.get(p1, 0):
            # 자기 자신을 부모 노드로 삼고
            parent[p1] = p1
            # 그 그룹에 속한 숫자를 1로 초기화
            number[p1] = 1
        # 마찬가지로 p2라는 친구가 parent에 없다면,
        if not parent.get(p2, 0):
            # 자기 자신을 부모 노드로 삼고
            parent[p2] = p2
            # 그 그룹에 속한 숫자를 1로 초기화
            number[p2] = 1
        # 이제 p1이 속한 그룹과 p2가 속한 그룹을 합쳐줄 차례
        print(union(p1, p2))


"""
def dfs(network, name, v):
    visited = v.copy()
    visited[name] = True
    stack = [name]

    while stack:
        p = stack.pop()

        for person in network.get(p):
            if not visited[person]:
                visited[person] = True
                stack.append(person)

    cnt = 0
    for key in visited.keys():
        a = visited.get(key)
        if a:
            cnt += 1

    return cnt


for tc in range(T):
    F = int(sys.stdin.readline())
    network = dict()
    visited_f = dict()
    for _ in range(F):
        p1, p2 = map(str, sys.stdin.readline().split())
        if not network.get(p1, 0):
            network[p1] = [p2]
        else:
            network[p1].append(p2)

        if not network.get(p2, 0):
            network[p2] = [p1]
        else:
            network[p2].append(p1)

        if not visited_f.get(p1, 0):
            visited_f[p1] = False

        if not visited_f.get(p2, 0):
            visited_f[p2] = False

        print(dfs(network, p1, visited_f))

시간초과 코드
"""