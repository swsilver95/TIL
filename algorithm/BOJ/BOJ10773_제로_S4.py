import sys


input = sys.stdin.readline
K = int(input())
data = []
for _ in range(K):
    data.append(int(input()))

def jaemin(numbers):
    stk = []
    for number in numbers:
        if number != 0:
            stk.append(number)
        else:
            stk.pop()
    return sum(stk)    
        
print(jaemin(data))