w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((p + t) // w) % 2 == 1:
    x = w - (p + t) % w
else:
    x = (p + t) % w

if ((q + t) // h) % 2 == 1:
    y = h - (q + t) % h
else:
    y = (q + t) % h

print(x, y)
