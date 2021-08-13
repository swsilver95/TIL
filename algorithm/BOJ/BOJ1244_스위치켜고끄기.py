n = int(input())
switches = list(map(int, input().split()))
s = int(input())

for student in range(s):
    sex, swc = map(int, input().split())
    if sex == 1:
        for i in range(swc - 1, len(switches), swc):    # 인덱스랑 swc 위치가 1 다르므로 swc - 1부터 swc의 배수만큼 작동
            switches[i] = int(not switches[i])          # 해당 위치의 스위치 작동
        # print(switches, 'boy')
    else:
        x = swc - 1                                     
        y = swc - 1                                        
        j = 0
        while True:
            nx = x - 1                                  # 앞뒤로 1씩 빼서 
            ny = y + 1 
            if nx < 0 or ny >= len(switches):
                break
            else:
                if switches[nx] == switches[ny]:        # 두 값이 같으면
                    x = nx                              # 스위치를 작동시킬 인덱스 첫값
                    y = ny                              # 스위치를 작동시킬 인덱스 마지막 값 지정
                    continue
                else:                                   # 같지 않다면
                    break                               # 바로 끝
        # print(x, y, 'x, y')                             # 디버깅용

        for k in range(x, y + 1):                       # switches의 x부터 y에 해당하는 인덱스들을 모두 작동
            switches[k] = int(not switches[k])

cnt = 0                                                 # 출력 횟수 카운팅
for switch in switches:             
    cnt += 1
    print(switch, end=' ')                              
    if cnt == 20:                                       # cnt가 20일 때마다 개행문자 출력
        print()
        cnt = 0