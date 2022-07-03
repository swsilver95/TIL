import sys
input = sys.stdin.readline

A1 = [
    [1, 1, 1, 1]
]

A2 = [
    [1],
    [1],
    [1],
    [1]
]

B1 = [
    [1, 1],
    [1, 1]
]

C1 = [
    [1, 0],
    [1, 0],
    [1, 1]
]

C2 = [
    [1, 1, 1],
    [1, 0, 0]
]

C3 = [
    [1, 1],
    [0, 1],
    [0, 1]
]

C4 = [
    [0, 0, 1],
    [1, 1, 1]
]

C5 = [
    [0, 1],
    [0, 1],
    [1, 1]
]

C6 = [
    [1, 0, 0],
    [1, 1, 1]
]

C7 = [
    [1, 1],
    [1, 0],
    [1, 0]
]

C8 = [
    [1, 1, 1],
    [0, 0, 1]
]

D1 = [
    [1, 0],
    [1, 1],
    [0, 1]
]

D2 = [
    [0, 1, 1],
    [1, 1, 0]
]

D3 = [
    [0, 1],
    [1, 1],
    [1, 0]
]

D4 = [
    [1, 1, 0],
    [0, 1, 1]
]

E1 = [
    [1, 1, 1],
    [0, 1, 0]
]

E2 = [
    [0, 1],
    [1, 1],
    [0, 1]
]

E3 = [
    [0, 1, 0],
    [1, 1, 1]
]

E4 = [
    [1, 0],
    [1, 1],
    [1, 0]
]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def solution(tet, B):
    r = len(B)
    c = len(B[0])
    height = len(tet)
    width = len(tet[0])
    
    max_val = 0
    for i in range(r - height + 1):
        for j in range(c - width + 1):
            tmp = 0
            for n in range(height):
                for m in range(width):
                   if tet[n][m]:
                       tmp += B[i + n][j + m] 
            
            if max_val < tmp:
                max_val = tmp
                
    return max_val


print(max(
    solution(A1, board),
    solution(A2, board),
    solution(B1, board),
    solution(C1, board),
    solution(C2, board),
    solution(C3, board),
    solution(C4, board),
    solution(C5, board),
    solution(C6, board),
    solution(C7, board),
    solution(C8, board),
    solution(D1, board),
    solution(D2, board),
    solution(D3, board),
    solution(D4, board),
    solution(E1, board),
    solution(E2, board),
    solution(E3, board),
    solution(E4, board)
    ))