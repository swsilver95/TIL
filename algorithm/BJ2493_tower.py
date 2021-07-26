import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
def laser(n, numbers):
    if n == 1: # 타워의 개수가 1개뿐이면 0을 리턴
        return 0
    
    stk = [] # 스택
    a = list(enumerate(numbers)) # 나중에 인덱스를 알아보기 편하게 하기 위해서 enumerate로 튜플형태로 만듦
    # print(a)
    lsr = [0] * n # 결과값을 저장할 리스트
    while len(a) > 0:
        if len(stk) == 0: # 스택에 아무 원소도 없으면 데이터의 맨 마지막에서 push
            stk.append(a.pop())
            # print(stk)
        if len(a) == 0: # 만약 a에 아무 원소도 남지 않으면 반복문 종료
            break

        if stk[-1][1] < a[-1][1]: # 스택의 마지막 값이 리스트의 마지막 값보다 작은 경우에는 레이저를 감지함.
            lsr[stk[-1][0]] = len(a) # 스택에서 빠지는 원소의 인덱스 위치에, 몇 번째 타워를 만났는지 lsr에 입력
            stk.pop() # 레이저를 만난 타워는 버림
        elif stk[-1][1] > a[-1][1]: # 스택의 마지막 값이 리스트의 마지막 값보다 크면 레이저를 감지할 수 없음.
            stk.append(a.pop()) # 그래서 일단 또 다음 타워에서 레이저를 쏨
    return ' '.join(map(str, lsr))


print(laser(N, towers))