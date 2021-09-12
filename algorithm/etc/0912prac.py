"""
N   trust   출력
2   [[1,2]]   2
3   [[1,3],[2,3]]   3
3   [[1,3],[2,3],[3,1]]   -1
3   [[1,2],[2,3]]   -1
4   [[1,3],[1,4],[2,3],[2,4],[4,3]]   3
"""
N = 3
trust = [[1,3],[2,3]]


def solution(N, trust):
    graph = [[] for _ in range(N + 1)]
    trusted = [0 for _ in range(N + 1)]

    for t in trust:
        graph[t[0]].append(t[1])
        trusted[t[1]] += 1

    for i in range(1, N + 1):
        if not graph[i]:
            if trusted[i] == N - 1:
                return i

    return -1


print(solution(N, trust))