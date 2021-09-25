from itertools import combinations
from collections import deque


def compare(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            cnt += 1

    if cnt == len(word1) - 1:
        return True
    else:
        return False


def solution(begin, target, words):
    words.append(begin)
    cases = list(combinations(words, 2))
    graph = {x: [] for x in words}

    for case in cases:
        w1, w2 = case
        if compare(w1, w2):
            graph[w1].append(w2)
            graph[w2].append(w1)

    q = deque()
    q.append(begin)
    visited = {y: 0 for y in words}
    visited[begin] = 1

    while q:
        p = q.popleft()
        if p == target:
            return visited[p] - 1

        for next_p in graph[p]:
            if not visited[next_p]:
                q.append(next_p)
                visited[next_p] = visited[p] + 1

    return 0
