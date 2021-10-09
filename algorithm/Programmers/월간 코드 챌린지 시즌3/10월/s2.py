def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = (i) // n + 1
        col = (i) % n + 1
        answer.append(max(row, col))

    return answer