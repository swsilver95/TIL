from collections import deque
import sys
input = sys.stdin.readline


T = int(input())

for tc in range(T):
    p = input().rstrip()
    n = int(input())
    my_list = deque(input().lstrip('[').rstrip(']\n').split(','))

    flag = True
    r = False
    try:
        for query in p:
            if query == 'R':
                r = not r
            else:
                if my_list and my_list != deque(['']):
                    if r:
                        my_list.pop()
                    else:
                        my_list.popleft()
                else:
                    raise AssertionError
    except AssertionError:
        flag = False

    if flag:
        if r:
            print('[' + ','.join(reversed(my_list)) + ']')
        else:
            print('[' + ','.join(my_list) + ']')

    else:
        print('error')
