from itertools import combinations


def solution(size):
    available = set()
    idx = list(range(1, size))
    cases = combinations(idx, 2)
    for case in cases:
        p1, p2 = case
        a = p1
        b = p2 - p1
        c = size - p2

        a, b, c = sorted([a, b, c])
        if c < a + b:
            available.add((a, b, c))
    return len(available)


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(50))
print(solution(99))
print(solution(100))

