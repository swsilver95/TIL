import sys

input = sys.stdin.readline

a = list(map(str, input().rstrip()))


def make_pal_even(name):
    name.sort()
    n = len(name)
    pal = [0] * n
    for i in range(n // 2):
        pal[i] = name[i * 2]
        pal[n - 1 - i] = name[i * 2 + 1]

    return ''.join(pal)


def make_pal_odd(name, target):
    name.sort()
    n = len(name)
    idx = name.index(target)
    name.pop(idx)
    pal = [0] * n
    pal[n // 2] = target
    for i in range(n // 2):
        pal[i] = name[i * 2]
        pal[n - 1 - i] = name[i * 2 + 1]

    return ''.join(pal)


def is_pal(name):
    n = len(name)
    check_str = list(set(name))
    if n % 2 == 0:  # n이 짝수일 때
        for i in check_str:
            if name.count(i) % 2:  # 개수가 홀수인 문자가 있다면
                return 'I\'m Sorry Hansoo'  # 생성 불가능
        else:
            return make_pal_even(name)

    else:  # n이 홀수일 때
        cnt = 0
        for i in check_str:
            if name.count(i) % 2:
                cnt += 1
                center_word = i
                if cnt > 1:
                    break

        if cnt != 1:  # 홀수 개수 문자가 1개가 아니라면
            return 'I\'m Sorry Hansoo'  # 생성 불가능
        else:
            return make_pal_odd(name, center_word)


print(is_pal(a))
