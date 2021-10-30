from itertools import combinations


def solution(logs):
    result = {}
    for log in logs:
        id, problem_id, score = map(int, log.split())
        if not result.get(id, 0):
            result[id] = [[-1] * 101, set(), 0]
            result[id][0][problem_id] = score
            result[id][1].add(problem_id)
            result[id][2] += score
        else:
            if result[id][0][problem_id] != -1:
                result[id][2] -= result[id][0][problem_id]
                result[id][0][problem_id] = score
                result[id][2] += score
            else:
                result[id][0][problem_id] = score
                result[id][2] += score
            result[id][1].add(problem_id)

    bad = set()
    cases = combinations(result, 2)
    for case in cases:
        p1 = result[case[0]]
        p2 = result[case[1]]
        if len(p1[1]) == len(p2[1]):
            if len(p1[1]) >= 5:
                if p1[1] == p2[1]:
                    if p1[2] == p2[2]:
                        bad.add(str(case[0]).zfill(4))
                        bad.add(str(case[1]).zfill(4))

    bad = list(bad)
    bad.sort()
    if len(bad) == 0:
        bad.append('None')

    return bad


print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]))
print(solution(["1901 10 50", "1909 10 50"]))