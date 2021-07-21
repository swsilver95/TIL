T = int(input())
dates = []
for _ in range(T):
    dates.append(input())

def my_dates(number):
    mon = int(number[4:6])
    date = int(number[6:8])
    if mon == 0:
        return(-1)
    elif mon == 2:
        if date > 28:
            return(-1)
    elif mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
        if date > 31:
            return(-1)
    else:
        if date > 30:
            return(-1)
    
    return(f'{number[:4]}/{number[4:6]}/{number[6:8]}')

for i in range(T):
    print(f'#{i + 1} {my_dates(dates[i])}')