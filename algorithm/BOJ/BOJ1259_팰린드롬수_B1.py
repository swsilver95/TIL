import sys
input = sys.stdin.readline

while True:
    number = input().rstrip()
    reversed_number = number[::-1]
    if number == '0':
        break

    if number == reversed_number:
        print('yes')
    else:
        print('no')
