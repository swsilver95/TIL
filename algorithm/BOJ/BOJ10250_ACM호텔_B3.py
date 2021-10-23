T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())     # H: 호텔 층수, W: 방 수, N: 몇 번째 손님
    h = (N - 1) % H + 1
    w = (N - 1) // H + 1
    w = str(w).zfill(2)

    print(str(h) + w)
