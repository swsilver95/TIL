T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)

    answer = ''
    for token in S:
        answer += token * R

    print(answer)