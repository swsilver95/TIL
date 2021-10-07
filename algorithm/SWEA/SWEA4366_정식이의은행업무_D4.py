T = int(input())


def search(b, t):
    b_set = set()
    t_set = set()

    for i in range(len(b)):
        tmp = b[:]
        if tmp[i] == '0':
            tmp[i] = '1'
        else:
            tmp[i] = '0'
        num = ''.join(map(str, tmp))
        b_set.add(int(num, 2))

    for j in range(len(t)):
        target = {'0', '1', '2'} - set(t[j])
        tmp = t[:]
        for a in target:
            tmp[j] = a
            num = ''.join(map(str, tmp))
            t_set.add(int(num, 3))

    return b_set & t_set


for tc in range(1, T + 1):
    b = list(input())
    t = list(input())
    answer = search(b, t)
    print('#{} {}'.format(tc, answer.pop()))