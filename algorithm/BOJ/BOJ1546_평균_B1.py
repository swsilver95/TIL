N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

new = []
for score in scores:
    tmp = score / max_score * 100
    new.append(tmp)

print(sum(new) / len(new))