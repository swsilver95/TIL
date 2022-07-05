N = int(input())

s = {i*i for i in range(1, int(100000 ** 0.5))}

def check(n):
    if n in s:
        return True
    return False


# 1
def solution(n):
    # 1
    if check(n):
        return 1
    
    # 2    
    for x in s:
        if N - x > 0:
            if check(N - x):
                return 2
            
    for i in s:
        for j in s:
            if N - i - j > 0:
                if check(N - i - j):
                    return 3
                
    return 4


print(solution(N))
