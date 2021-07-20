'''
n개의 정수로 이루어진 임의의 수열이 주어진다. 
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 
단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 
여기서 정답은 12+21인 33이 정답이 된다.

첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 
둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
첫째 줄에 답을 출력한다.

입력 예시 1)
10
10 -4 3 1 5 6 -35 12 21 -1

출력 예시 1)
33

'''
import sys

n = sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().split(" ")))

my_list = [numbers[0]] # max로 정답을 출력할 리스트, for 연산을 1부터 시작할 것이므로 [0]값을 미리 할당
tmp = numbers[0] # 리스트에서 직접적으로 더하거나 비교할 값

for number in numbers[1:]: # 첫 번째 값을 제외한 list 내 항목들에 대해
    if tmp < 0: # tmp가 음수인 경우,
        tmp = number # 더이상 tmp에 데이터를 더할 필요가 없으므로 tmp 값을 number로 바꿔버림
    else: # 그런데 tmp가 음수는 아닌 경우
        tmp = tmp + number # 일단 더해봄

    my_list.append(tmp) # tmp vs. numbers[0] 중에서 누가 큰지 모르니까 일단 리스트에 넣음 
    
print(max(my_list)) # my_list에서 가장 큰 값을 출력함


'''
sumlist = []
stk = []
for i in range(len(data)):
    tmp = data[i]
    for j in range(i, len(data)):
        if i == j:
            stk.append(data[i])
        tmp += data[j]
        if stk[-1] < tmp:
            stk.append(tmp)
        else:
            pass
    sumlist.append(stk[-1])
    stk = [0]

print(max(sumlist))
'''
