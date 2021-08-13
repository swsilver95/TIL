'''
수빈이는 동생 N명과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.
수빈이는 걸어서 이동을 할 수 있다. 
수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 
수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.
모든 동생을 찾기위해 D의 값을 정하려고 한다. 
가능한 D의 최댓값을 구해보자.

첫째 줄에 N(1 ≤ N ≤ 105)과 S(1 ≤ S ≤ 109)가 주어진다. 
둘째 줄에 동생의 위치 Ai(1 ≤ Ai ≤ 109)가 주어진다. 
동생의 위치는 모두 다르며, 수빈이의 위치와 같지 않다.
가능한 D값의 최댓값을 출력한다.

예제 입력 1)
3 3
1 7 11

예제 출력 1)
2

'''

N, S = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

num_list = []
for i in range(N):
    num_list.append(abs(data[i] - S))
'''
def find_D(data):
    global num_list
    global N
    for j in range(min(num_list), 1, -1):
        count = 0
        for k in num_list:
            if k % j == 0:
                count += 1
            if count == N:
                return(j)

ans = find_D(data)
print(ans)
'''

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
    
if N == 1:
    print(num_list[0])
else:
    a = gcd(num_list[0], num_list[1])
    for j in range(N):
        a = gcd(a, num_list[j])
    print(a)