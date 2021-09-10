def solution(v):
    x = []
    y = []
    for p in v:
        x.append(p[0])
        y.append(p[1])

    for i in x:
        if x.count(i) == 1:
            nx = i

    for j in y:
        if y.count(j) == 1:
            ny = j

    return [nx, ny]



v = [[1, 1], [2, 2], [1, 2]]
print(solution(v))