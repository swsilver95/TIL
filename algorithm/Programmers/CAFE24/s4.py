def solution(num):
    # return '홀' if num % 2 else '짝'
    if num % 2:
        answer = '홀'
    else:
        answer = '짝'
    return answer


print(solution(3))
print(solution(8))
print(solution(11010101))
