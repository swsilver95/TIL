import sys 
input = sys.stdin.readline


N = int(input())
mats = [list(map(int, input().split())) for _ in range(N)]

ans = 1e10
for i in range(1, 2 ** N):
    b = bin(i)[2:].zfill(N)
    
    sour = 1
    bitter = 0
    
    for idx in range(N):
        if b[idx] == '1':
            x, y = mats[idx]
            sour *= x
            bitter += y
    
    diff = abs(sour - bitter)
    if diff < ans:
        ans = diff
        
print(ans)
