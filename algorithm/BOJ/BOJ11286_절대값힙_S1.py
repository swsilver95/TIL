import sys
from heapq import *
input = sys.stdin.readline

N = int(input())

h_pos = []
h_neg = []

def solution(n):
    for i in range(n):
        c = int(input())
        
        if c == 0:
            if len(h_pos) == 0 and len(h_neg) == 0:
                print(0)
                continue
            
            elif len(h_pos) == 0 and len(h_neg) != 0:
                print(-heappop(h_neg))
                
            elif len(h_pos) != 0 and len(h_neg) == 0:
                print(heappop(h_pos))
                
            else:
                a = h_pos[0]
                b = h_neg[0]
                        
                if a < b:
                    print(heappop(h_pos))
                else:
                    print(-heappop(h_neg))
                
        elif c > 0:
            heappush(h_pos, c)
            
        else:
            heappush(h_neg, -c)

solution(N)

