T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    max_scores = sum(scores)
    available = [False] * (max_scores + 1)
    available[0] = True
    numbers = [0]

    for score in scores:
        k = len(numbers)
        for i in range(k):
            tmp = numbers[i] + score
            if tmp > max_scores:
                continue

            if not available[tmp]:
                numbers.append(tmp)
                available[tmp] = True

    print('#{} {}'.format(tc, len(numbers)))