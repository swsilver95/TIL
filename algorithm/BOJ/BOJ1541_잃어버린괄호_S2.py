formula = input()

tokens = formula.split('-')
computed = []
for token in tokens:
    tmp = list(map(int, token.split('+')))
    computed.append(sum(tmp))

answer = computed[0]
if len(computed) > 1:
    for idx in range(1, len(computed)):
        answer -= computed[idx]

print(answer)
