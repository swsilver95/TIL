from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def bfs(start):
    q = deque()
    visited = [-1] * (N + 1)
    visited[start] = 0
    q.append(start)

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)

    answer = 0
    for i in range(N + 1):
        if visited[i] > 0:
            answer += visited[i]

    # print(visited)
    return answer


min_bacon = 1e9
person = 0
for k in range(1, N + 1):
    tmp = bfs(k)
    if min_bacon > tmp:
        min_bacon = tmp
        person = k

print(person)
