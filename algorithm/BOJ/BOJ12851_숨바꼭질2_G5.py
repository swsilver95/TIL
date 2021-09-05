from collections import deque

N, K = map(int, input().split())    # N은 현재 수빈의 위치, K는 동생의 위치
'''
이동 방향은 세 가지가 가능
-1 / +1 / *2
'''


def bfs(N, K):
    q = deque()
    q.append(N)
    global cnt

    while q:
        p = q.popleft()
        # 도착했다면, 최단 거리로 도착한 방법 수에 + 1
        if p == K:
            cnt += 1
            
        # p에서 이동할 수 있는 방법은 총 세 가지
        p_available = [p - 1, p + 1, p * 2]
        for next_p in p_available:
            # 다음 p의 위치가 정상적인 위치에 있다면,
            if 0 <= next_p < 100001:
                # 1. 방문하지 않은 곳이거나,
                # 2. 이미 방문했던 곳인데, 계산상 도착할 시간이 똑같다면
                if not visited[next_p] or visited[next_p] == visited[p] + 1:
                    visited[next_p] = visited[p] + 1
                    q.append(next_p)


cnt = 0                                 # 개수는 0으로 우선 초기화
visited = [0 for _ in range(100001)]    # 방문처리할 배열
visited[N] = 1                          # 시작점 방문처리
bfs(N, K)                               # 너비우선탐색 시작

print(visited[K] - 1)                   # K에 도착했을 때의 최단 시간 출력 / 시작점이 1이었으므로, 최종 결과에서 1을 뺌
print(cnt)                              # 최단 시간으로 몇 번 K를 찾아냈는지 출력