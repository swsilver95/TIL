import sys

sys.stdin = open('input.txt')

T = int(input())


def alien(nambers):                              # 정렬할 문자열 리스트를 입력받아 정렬할 결과를 출력
    nam = ["ZRO", "ONE", "TWO", "THR", "FOR",
           "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(10):                             # 리스트를 총 10번 순회할 예정
        for namber in nambers:                      # 정렬할 문자열 리스트에서
            if namber == nam[i]:                    # 순서대로 출력
                print(namber, end=' ')


for _ in range(1, T + 1):
    tc, n = map(str, input().split())
    N = int(n)
    data = list(map(str, input().split()))
    print(tc)
    alien(data)
    print()