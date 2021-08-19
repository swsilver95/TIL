import sys

sys.stdin = open('input.txt')

def get_solution2(arr, m):
    for word in arr:  # 1 ~ 100
        for s in range(100 - m + 1):
            for k in range(m // 2):
                if word[s + k] != word[s + m - 1 - k]:
                    break
            else:
                return m
    return 0


T = 10
for _ in range(1, T + 1):
    t = int(input())
    a = [input() for _ in range(100)]
    b = [''.join(x) for x in zip(*a)]

    maxLength = 1
    for m in range(2, 101):
        if m > maxLength + 2: break
        if maxLength < get_solution2(a, m):
            maxLength = m

    m = maxLength + 1
    for m in range(maxLength + 1, 101):
        if m > maxLength + 2: break
        if maxLength < get_solution2(b, m):
            maxLength = m

    print('#%d %s' % (t, maxLength))