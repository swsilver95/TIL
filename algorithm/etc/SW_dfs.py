# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:37:50 2021

@author: seung
"""

t = int(input())

for i in range(t):
    x = i + 1
    count = 0
    n = int(input())
    data = list(map(int, input().split(" ")))
    visited = [False] * (n + 1)
    ans = [0] * n
    
    def dfs(idx):
        global count
        global n
        global ans
        if idx == n:
            count += 1
            print(ans, "정답")
            ans = [0] * n
            return
    
        check = True
        for s in range(1, n + 1):
            if not visited[s] and data[idx] != s:
                visited[s] = True
                ans[idx] = s
                print(ans)
                dfs(idx + 1)
                visited[s] = False
                check = False
        if check:
            print("실패")
            
dfs(0)
print("#%d %d"%(x, count))
print("----------------------------------")