'''
★ 4
● 3
■ 2
▲ 1

'''
def card_game(a_card, b_card):
    a = [0] * 5
    b = [0] * 5
    for card in a_card:
        a[card] += 1
    for card in b_card:
        b[card] += 1

    if a[4] > b[4]:
        return 'A'
    elif a[4] < b[4]:
        return 'B'
    else:
        if a[3] > b[3]:
            return 'A'
        elif a[3] < b[3]:
            return 'B'
        else:
            if a[2] > b[2]:
                return 'A'
            elif a[2] < b[2]:
                return 'B'
            else:
                if a[1] > b[1]:
                    return 'A'
                elif a[1] < b[1]:
                    return 'B'
                else:
                    return 'D'

N = int(input())
for _ in range(N):
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_card = a_list[1:]
    b_card = b_list[1:]
    print(card_game(a_card, b_card))