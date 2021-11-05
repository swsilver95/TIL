def solution(numArr):
    k, m, e = numArr
    avg = (k + m + e) / 3

    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'

    answer = list()
    avg = '{:.2f}'.format(avg)
    answer.append(avg)
    answer.append(grade)

    return answer


print(solution([100, 100, 98]))
print(solution([100, 100, 100]))