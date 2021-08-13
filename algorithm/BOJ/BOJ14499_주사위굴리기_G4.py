# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:36:01 2021

@author: seung
"""
#(세로 n X 가로 m) 격자
global dice
global data
global location
global n
global m
global k

n, m, x, y, k = map(int, input().split(" "))
data = [[0] * m for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split(" ")))
    for j in range(m):
        data[i][j] = tmp[j]

order = list(map(int, input().split(" ")))

# print(data)
dice = [[0] * 3 for _ in range(4)]

location = [x, y]

'''
전개도
 [[x][x], [0][1], [x][x]] 
 [[1][0], [1][1], [1][2]] 
 [[x][x], [2][1], [x][x]]
 [[x][x], [3][1], [x][x]]
'''
def north():
    if location[0] == 0:
        return
    
    elif location[0] != 0:
        location[0], location[1] = location[0] - 1, location[1]
        if data[location[0]][location[1]] == 0:
            data[location[0]][location[1]] = dice[0][1]
            
        elif data[location[0]][location[1]] != 0:
            dice[0][1] = data[location[0]][location[1]]
            data[location[0]][location[1]] = 0
        
        dice[3][1], dice[2][1], dice[1][1], dice[0][1] = dice[0][1], dice[3][1], dice[2][1], dice[1][1] 
        print(dice[1][1])
        
        
def east():
    if location[1] == m-1:
        return
    
    elif location[1] != m-1:
        location[0], location[1] = location[0], location[1] + 1
        if data[location[0]][location[1]] == 0:
            data[location[0]][location[1]] = dice[1][2]
            
        elif data[location[0]][location[1]] != 0:
            dice[1][2] = data[location[0]][location[1]]
            data[location[0]][location[1]] = 0
            
        dice[3][1], dice[1][0], dice[1][1], dice[1][2] = dice[1][2], dice[3][1], dice[1][0], dice[1][1]   
        print(dice[1][1])


def west():
    if location[1] == 0:
        return
    
    elif location[1] != 0:
        location[0], location[1] = location[0], location[1] - 1
        if data[location[0]][location[1]] == 0:
            data[location[0]][location[1]] = dice[1][0]
            
        elif data[location[0]][location[1]] != 0:
            dice[1][0] = data[location[0]][location[1]]
            data[location[0]][location[1]] = 0
            
        dice[3][1], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[3][1] 
        print(dice[1][1])
        
        
def south():
    if location[0] == n-1:
        return
    
    elif location[0] != n-1:
        location[0], location[1] = location[0] + 1, location[1]
        if data[location[0]][location[1]] == 0:
            data[location[0]][location[1]] = dice[2][1]
            
        elif data[location[0]][location[1]] != 0:
            dice[2][1] = data[location[0]][location[1]]
            data[location[0]][location[1]] = 0
            
        dice[3][1], dice[2][1], dice[1][1], dice[0][1] = dice[2][1], dice[1][1], dice[0][1], dice[3][1] 
        print(dice[1][1])
        
def process_order(order):
    for i in order:
        if i == 1:
            east()
        elif i == 2:
            west()
        elif i == 3:
            north()
        elif i == 4:
            south()
            
process_order(order)

# %%
'''
from collections import deque

dice = [0, 0, 0, 0, 0, 0]
n, m, x, y, k = map(int, input().split(" "))
data = [[0] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split(" ")))
    for j in range(m):
        data[i][j] = tmp[j]

tmp = list(map(int, input().split(" ")))

q = deque()  # 덱에 대입
for i in tmp:
    q.append(i)

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def checkZero(firstIndex, secondIndex):  # 바닥이 0인지 확인하는 함수
    if data[firstIndex][secondIndex] == 0:
        return True
    return False


def turn(dir):  # 주사위를 회전하는 함수
    global dice
    if dir == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]

    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]

    elif dir == 3:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

    elif dir == 4:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]


ans = []
while q:  # 입력된 모든 값을 통해 연산
    dir = q.popleft()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 밖을 가마녀
        continue  # 연산에서 제외

    x, y = nx, ny  # 밖을 나가지 않았으므로 x, y에 값 대입
    turn(dir)
    if checkZero(x, y):  # 땅이 0이면
        data[x][y] = dice[5]  # 주사위가 위치하는 면에 밑면의 값을 복사

    elif not checkZero(x, y):  # 땅이 0이 아니면
        dice[5] = data[x][y]  # 주사위의 밑면에 주사위가 위치하는 면의 값을 복사하고,
        data[x][y] = 0  # 주사위가 위치하는 면의 값을 0으로 변경

    ans.append(dice[0])  # 연산에서 얻은 윗면의 값을 추가

for an in ans:
    print(an)
'''