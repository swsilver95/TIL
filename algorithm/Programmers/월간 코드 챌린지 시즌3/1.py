def solution(numbers):
    total = 0
    for i in range(1, 10):
        if i not in numbers:
            total += i
    return total