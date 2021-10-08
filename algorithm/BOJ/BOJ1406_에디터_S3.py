import sys

input = sys.stdin.readline
s1 = [*input().rstrip()]
s2 = []

for _ in range(int(input())):
    tmp = input().rstrip().split()
    if tmp[0] == 'P':
        s1.append(tmp[1])
    elif tmp[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif tmp[0] == 'D':
        if s2:
            s1.append(s2.pop())
    else:
        if s1:
            s1.pop()

s2.reverse()
s1 = s1 + s2
print(''.join(s1))
