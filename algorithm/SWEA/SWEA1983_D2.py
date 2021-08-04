grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    print(f'#{idx + 1}', end=' ')

    scores = []
    for i in range(N):
        mid, fin, hw = map(int, input().split())
        total = mid * 0.35 + fin * 0.45 + hw * 0.2
        scores.append((total, i+1))
        if i+1 == K:
            target = (total, i+1)
    scores.sort(reverse=True)
    # print(scores)
    # print(target)
    rnk = scores.index(target)
    rnk_idx = int((rnk / N) * 10)
    # print(rnk)
    print(grade[rnk_idx])