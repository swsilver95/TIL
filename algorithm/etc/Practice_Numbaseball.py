# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 20:24:37 2021

@author: seung
"""

# %% Number Baseball Game
from random import randint
from itertools import permutations

def Create_Number(): # 서로 다른 네자리 숫자를 임의로 생성하는 함수
    N = list(range(1,10)) 
    N_p = list(permutations(N, 4)) # 순열을 이용해서 중복된 숫자 없는 리스트 생성
    Ran_num = randint(0, len(N_p) - 1) 
    Select = N_p[Ran_num] # N_p의 임의의 원소를 하나 선택
    Answer = int("{0}{1}{2}{3}".format(Select[0], Select[1], Select[2], Select[3])) #
    return Answer # 네자리 숫자를 반환
    


def BaseGame(): # 입력값을 받아서 야구게임을 시작
    num = input("네 자리 숫자를 입력하세요(중복된 숫자는 없습니다): ")
    global Answer # Answer를 전역변수로 사용
        
    if (num.isdigit() * len(str(num)) == 4) == False:
        print("네자리 숫자만 입력이 가능합니다.")
        return BaseGame()
    
    num_map = list(map(int, num))
    Answer_map = list(map(int, str(Answer)))
    Strike = 0
    common_num = [x for x in num_map if x in Answer_map] # 입력된 수와 정답 간의 공통된 숫자를 리스트로 만듦
        
    if len(common_num) == 0: # 공통 숫자가 없을 경우에는 0볼, 0스트라이크 출력
        print("0 볼, 0 스트라이크")
        return BaseGame()
            
    
    for i in range(0, 4): # Strike 개수 탐색
        if num_map[i] == Answer_map[i]:
            Strike += 1
                        
    if Strike == 0: # Strike가 없을 경우
        print("입력하신 숫자: {0}은(는) {1} 볼, 0 스트라이크입니다.".format(num, len(common_num)))
        return BaseGame()
                
    elif 0 < Strike < 4 : # Strike가 있을 경우
        print("입력하신 숫자: {0}은(는) {1} 볼, {2} 스트라이크입니다.".format(num, len(common_num) - Strike, Strike))
        return BaseGame()
            
    print("입력하신 숫자: {0}은(는) 정답입니다!".format(num))

Answer = Create_Number()
print(Answer)
BaseGame()
