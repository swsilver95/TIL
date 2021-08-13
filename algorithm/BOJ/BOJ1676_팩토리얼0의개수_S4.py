'''
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
첫째 줄에 구한 0의 개수를 출력한다.

입력 예시 1)
10

출력 예시 1)
3
'''

num = int(input())

count = 0
for i in range(5, num + 1, 5):
    if i % 125 == 0:
        count += 3
    elif i % 25 == 0:
        count += 2
    else:
        count += 1
print(count)