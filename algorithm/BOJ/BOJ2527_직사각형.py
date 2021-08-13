def square_test(x1, y1, p1, q1, x2, y2, p2, q2):        # x좌표를 기준으로 생각
    if x2 < x1:                                         # 두 번째 직사각형의 x좌표가 첫 번째 직사각형의 x좌표보다 작은 경우
        if p2 < x1 or q2 < y1:                          # 겹치는 부분이 없는 케이스
            return 'd'
        if p2 == x1 and q2 == y1:                       # 한 점에서 만나는 케이스
            return 'c'
        if p2 == x1 and q2 > y1:                        # 선분으로 만나는 케이스
            return 'b'
        if p2 > x1 and q2 == y1:                        # 선분으로 만나는 케이스
            return 'b'
        else:                                           # 이외의 경우에는 모두 직사각형
            return 'a'
    elif x1 <= x2 < p1:                                 # 두 직사각형의 x좌표가 같을 경우
        if q2 < y1 or y2 > q1:                          # 겹치는 부분이 없는 케이스
            return 'd'                              
        if q2 == y1 or y2 == q1:                        # 선분으로 만나는 케이스
            return 'b'
        else:                                           # 이외의 경우에는 모두 직사각형
            return 'a'
    elif x2 == p1:
        if y2 > q1 or q2 < y1:                          # 겹치는 부분이 없는 케이스
            return 'd'
        if q2 == y1 or q1 == y2:                        # 한 점에서 만나는 케이스
            return 'c'
        else:                                           # 이외의 경우는 모두 선분으로 만나는 케이스
            return 'b'
    else:
        return 'd'

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    print(square_test(x1, y1, p1, q1, x2, y2, p2, q2))
