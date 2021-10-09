def dfs(numbers, n, idx, value, target, visited):
    global cnt
    if idx == n:
        if value == target:
            cnt += 1
        return

    if not visited[idx]:
        visited[idx] = True
        dfs(numbers, n, idx + 1, value + numbers[idx], target, visited)
        dfs(numbers, n, idx + 1, value - numbers[idx], target, visited)
        visited[idx] = False


cnt = 0


def solution(numbers, target):
    global cnt
    n = len(numbers)
    visited = [False for _ in range(n)]
    answer = 0
    dfs(numbers, n, 0, 0, target, visited)
    return cnt