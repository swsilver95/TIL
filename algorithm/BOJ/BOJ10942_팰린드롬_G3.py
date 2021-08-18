import sys

input = sys.stdin.readline


def find_palindrome(numbers):
    n = len(numbers)
    for i in range(2000):
        d[i][i] = True                                          # 길이가 1인 친구는 항상 회문

    target_length = 2                                           # 길이가 2인 회문은 그냥 둘이 같을 때
    for i in range(n - target_length + 1):
        if numbers[i] == numbers[i + 1]:
            d[i][i + 1] = True

    for target_length in range(3, n + 1):                       # 길이가 짧은 회문부터 찾으면서 d 배열에 True를 추가
        for i in range(n - target_length + 1):
            if numbers[i] == numbers[i + target_length - 1]:    # 반복을 돌다가 첫값하고 끝값이 같은 친구를 만나면
                if d[i + 1][i + target_length - 2]:             # 그 바로 안쪽 친구가 회문일 경우에
                    d[i][i + target_length - 1] = True          # 얘도 회문
    return d


N = int(input())
numbers = list(map(int, input().split()))
d = [[False] * 2000 for _ in range(2000)]
M = int(input())
# print(d)
find_palindrome(numbers)
for _ in range(M):
    n, m = map(int, input().split())
    if d[n-1][m-1]:
        # print(numbers[n-1:m])
        print(1)
    else:
        # print(numbers[n-1:m])
        print(0)
