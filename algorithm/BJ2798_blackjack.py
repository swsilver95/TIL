# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:32:25 2021

@author: seung
"""

# %% 11057
from itertools import combinations

n, target = map(int, input().split(" "))
cardlist = list(map(int, input().split(" ")))

def comb(all_cardlist):
    all_cardlist = list(combinations(cardlist, 3))
    sum_list = []
    for i in all_cardlist:
        sum_list.append(sum(i))
    return sum_list

def findtarget(sum_list):
    global target
    subtract_list = []
    
    for i in sum_list:
        if i - target <= 0:
            subtract_list.append(target - i)
        
        elif i - target > 0:
            subtract_list.append(100001)
            
    n = min(subtract_list)
    k = subtract_list.index(n)
    
    print(sum_list[k])

sum_list = comb(cardlist)
Answer = findtarget(sum_list)

'''
import itertools

n, m = map(int, input().split(" "))  # n과 m을 입력받음
data = list(map(int, input().split(" ")))  # 카드의 목록을 입력받음
ans = list(itertools.combinations(data, 3))  # itertools 의 combinations 를 이용하여 정답이 가능한 쌍 모두 출력
pre = 0
for i in ans:  # 모든 정답에 관하여 처리
    if pre < sum(i) <= m:
        pre = sum(i)
        if pre == m:
            break
print(pre)  # 정답 출력
'''