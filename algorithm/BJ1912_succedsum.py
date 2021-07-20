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

stk = [numbers[0]]
tmp = numbers[0]

for number in numbers[1:]:
    if tmp < 0:
        tmp = number
    else:
        tmp = tmp + number

    stk.append(tmp)
    
print(max(stk))