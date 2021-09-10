
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []
    new = progresses[:]
    flag = True
    while flag:
        for i in range(len(new) - 1, -1, -1):
            new[i] = new[i] + speeds[i]
        if new[0] >= 100:
            j = 0
            while new[j] >= 100:
                j += 1
                if j == len(new):
                    answer.append(j)
                    return answer
            answer.append(j)
            new = new[j:]
            speeds = speeds[j:]
            continue
    return answer


print(solution(progresses, speeds))