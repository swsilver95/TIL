import sys
sys.stdin = open('input.txt')

T = int(input())

'''
가위 1
바위 2
보   3


    0 1 2 3
    _ _ _ _
0 | 0 0 0 0
1 | 0 1 2 1
2 | 0 1 1 2
3 | 0 2 1 1
'''

check = [[0, 0, 0, 0],
         [0, 1, 2, 1],
         [0, 1, 1, 2],
         [0, 2, 1, 1]]


def compare_cards(tup1, tup2):
    card1 = tup1[1]
    card2 = tup2[1]
    if check[card1][card2] == 1:
        return tup1
    elif check[card1][card2] == 2:
        return tup2


def winner(numbers):
    if len(numbers) == 1:
        return numbers[0]

    # 킹륜기: 놀랍게도 이 부분은 필요가 없다.
    # if len(numbers) == 2:
    #     return compare_cards(numbers[0], numbers[1])

    n = len(numbers)
    start = 0
    end = n - 1
    mid = (start + end) // 2
    numbers_left = numbers[:mid+1]
    numbers_right = numbers[mid+1:]
    return compare_cards(winner(numbers_left), winner(numbers_right))


for tc in range(1, T + 1):
    N = int(input())
    tmp = list(map(int, input().split()))
    cards = list(enumerate(tmp, start=1))
    # print(cards)
    win = winner(cards)
    print('#{} {}'.format(tc, win[0]))