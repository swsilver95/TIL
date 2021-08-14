def count_stick(x):
    check = []
    ans = 0
    for i in range(len(x)):
        if x[i] == "(":
            check.append("(")
        elif x[i] == ")":
            if x[i - 1] == "(":
                check.pop()
                ans += len(check)
            elif x[i - 1] ==")":
                check.pop()
                ans += 1
    return(ans)

T = int(input())

for tc in range(1, T + 1):
    data = input()
    print('#{}'.format(tc), end=' ')
    print(count_stick(data))