T = int(input())
d = []
datum = []
for _ in range(T):
    d.append(int(input().rstrip()))
    datum.append(list(map(int, input().split(' '))))

def money(total, my_list):
    if len(my_list) <= 1:
        return total

    earn = total
    price_max = max(my_list)
    idx = my_list.index(price_max)
    buy_list = my_list[:idx + 1]
    # print(buy_list)
    earn += len(buy_list) * price_max - sum(buy_list)
    # print(earn)
    if len(buy_list) == len(my_list):
        return earn
    else:
        return money(earn, my_list[idx + 1:])

for i in range(T):
    print(f'#{i+1} {money(0, datum[i])}')

import heapq

t = int(input())
for i in range(t):
    x = i + 1
    n = int(input())
    data = list(map(int, input().split()))
    q = []
    ans = 0
    '''
    은을 위한 자료구조 우선순위 큐 중 minHeapq
    힙 큐에 자료를 넣으면 트리 구조로 트리의 최상단 (0번 자리에) 최솟값이 존재함
    중요 : heappush 로 넣어야함
    heapq.heappush(배열, 넣을 것)
    만약 배열을 넣을경우 heapify인가 써서 heap으로 만들어야함
    heapq.heapify(배열)
    -> 이문제의 경우 순서가 있으므로 배열 전체를 넣으면 안됨
    최상단 원소를 보는법 배열[0]
    최상단 원소를 끄내는 법 heapq.heappop(배열)
    중요 : 힙은 최상단만 최솟값이고 나머지 순서는 작은 힙의 구조로 이루어져 있어서 오름차순이 아님
    -> 언제 쓰냐????? 이건 제 좀 경험인데 모든 값을 정렬안하고 최솟값위주로 연산이 필요한경우 사용함
    
    이 문제를 보면
    2 번 케이스의 3 5 9 가 매우 큰 힌트임
    3원짜리를 5원에 팔고 5원에 2개사고 9원에 2개 팔아도 얻을 이득의 최댓값이 동일함
    증명은 알아서 하기 ㄱ임
    ==> 따라서 이 케이스를 생각해서 구현하면 답이 쉽게 나옴 
    '''
    heapq.heappush(q, data[0])  # 스타트를 위해 첫 데이터를 넣음
    for i in range(1, n):
        while q[0] < data[i]:  # 트리의 최상단이 data 보다 작으면
            ans += data[i] - heapq.heappop(q)  # 정답에 추가하고 힙에서 제외
            heapq.heappush(q, data[i])  # 다시 데이터의 크기 만큼 넣음
        heapq.heappush(q, data[i])  # 이제 data를 넣음
    print("#" + str(x) + ' ' + str(ans))