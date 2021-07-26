T = int(input())
my_strings = []
for _ in range(T):
    my_strings.append(input())

def madi(my_str):
    i = 1
    compare = my_str[0:i]
    while compare != my_str[i:i*2]:
        i += 1
        if my_str[0:i] == my_str[i:i*2]:
            left = my_str.replace(my_str[0:i], '')
            if left in my_str[0:i]:
                key = my_str[0:i]
                return len(key)
    return 0

for i in range(T):
    print(f'#{i+1} {madi(my_strings[i])}')