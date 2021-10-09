def solution(n, m, x, y, queries):
    a1, b1, a2, b2 = x, y, x, y
    while queries:
        q = queries.pop()
        a1, b1, a2, b2 = moving(n, m, a1, b1, a2, b2, q)
        if [a1, b1, a2, b2] == [-1, -1, -1, -1]:
            return 0
    return (a2 - a1 + 1) * (b2 - b1 + 1)


def moving(n, m, x1, y1, x2, y2, query):
    direction = query[0]
    step = query[1]
    if direction == 0:
        if y1 == 0:
            y2 = min(y2 + step, m - 1)
        elif y1 + step > m - 1:
            return [-1, -1, -1, -1]
        else:
            y1 += step
            y2 = min(y2 + step, m - 1)
    elif direction == 1:
        if y2 == m - 1:
            y1 = max(0, y1 - step)
        elif y2 - step < 0:
            return [-1, -1, -1, -1]
        else:
            y1 = max(0, y1 - step)
            y2 -= step
    elif direction == 2:
        if x1 == 0:
            x2 = min(x2 + step, n - 1)
        elif x1 + step > n - 1:
            return [-1, -1, -1, -1]
        else:
            x1 += step
            x2 = min(x2 + step, n - 1)
    else:
        if x2 == n - 1:
            x1 = max(x1 - step, 0)
        elif x2 - step < 0:
            return [-1, -1, -1, -1]
        else:
            x1 = max(x1 - step, 0)
            x2 -= step
    return [x1, y1, x2, y2]