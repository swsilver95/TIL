# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:22:26 2021

@author: seung
"""
# %% 9095

N = int(input())
case = []
for _ in range(N):
    case.append(int(input()))
    
def ans(N):
    if N == 1:
        return 1
    
    if N == 2:
        return 2
        
    if N == 3:
        return 4
    
    if N >= 4:
        return ans(N - 1) + ans(N - 2) + ans(N - 3)
    
for i in case:
    k = ans(i)
    print(k)