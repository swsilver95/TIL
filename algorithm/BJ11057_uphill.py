# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 00:27:27 2021

@author: seung
"""
'''
N = int(input())

def count_ascending_num(x):
    all_num = range(10**(x-1), 10**x)
    num = 0
    for i in all_num:
        num_map = list(map(int, str(i)))
        count = 0
        j = 0
        while j in range(len(num_map) - 1):
            if num_map[j] <= num_map[j+1]:
                count += 1
                j += 1
            elif num_map[j] > num_map[j+1]:
                j += 1
        if count == len(num_map) - 1:
            num += 1
    
    print(num)
    return(num)

count_ascending_num(N)   
'''

import math

N = int(input())

def count_ascending_num(N):
    if N == 1:
        return 10
        
    Ans = math.comb(9 + N, 9)
    return Ans
  
Ans = count_ascending_num(N)
print(Ans%10007)

# %%

n = int(input())

# n X 10의 행렬 만들기
uphill = [[0] * 10 for _ in range(n + 1)]

# 0~9로 시작하는 한자리 숫자의 개수 = 1
uphill[1] = [1] * 10

for i in range(2, n + 1):
    # 0으로 끝나는 i자리 숫자의 개수 = 1
    uphill[i][0] = 1

    for j in range(10):
        uphill[i][j] = uphill[i - 1][j] + uphill[i][j - 1]

print(sum(uphill[n]) % 10007)