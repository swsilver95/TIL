N = int(input())
clap = [3, 6, 9]

for i in range(1, N+1):
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        tmp = list(map(int, str(i)))
        cnt3 = tmp.count(3)
        cnt6 = tmp.count(6)
        cnt9 = tmp.count(9)
        print('-' * (cnt3 + cnt6 + cnt9), end=' ')
    else:
        print(i, end=' ') 
