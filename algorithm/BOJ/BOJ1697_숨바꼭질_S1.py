from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        p = q.popleft()
        if p == K:
            return visited[p] - 1

        for next_p in [p - 1, p + 1, 2 * p]:
            if 0 <= next_p <= 100000:
                if not visited[next_p]:
                    q.append(next_p)
                    visited[next_p] = visited[p] + 1


print(bfs(N))