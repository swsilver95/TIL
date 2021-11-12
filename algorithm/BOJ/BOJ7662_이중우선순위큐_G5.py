from heapq import *
from collections import defaultdict
import math
import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    min_heap = []
    max_heap = []
    num_count = defaultdict(int)
    cnt = 0
    k = int(input().rstrip())

    for _ in range(k):
        command, num = map(str, input().rstrip().split())
        num = int(num)

        # 1. 'I' 가 입력으로 주어질 경우 num을 최소힙, 최대힙에 각각 추가
        #    이 때, 힙에 사용된 숫자의 개수를 저장하는 딕셔너리에 카운트 1을 추가
        #    전체 숫자 개수 cnt에 1 추가
        if command == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
            num_count[num] += 1
            cnt += 1

        # 2. 'D' 가 입력으로 주어졌을 때,
        else:
            # 2.1. 힙에 들어있는 숫자가 없다면 해당 연산 무시하고 두 힙을 모두 초기화
            if cnt == 0:
                min_heap = []
                max_heap = []
                continue

            # 2.2. 힙에 들어있는 숫자가 있다면,
            # 3. 최댓값을 찾아서 삭제하는 연산일 경우
            if num == 1:
                while True:
                    # 3.1. 힙에서 최댓값을 뽑아서 tmp에 저장하고
                    tmp = -heappop(max_heap)
                    # 3.2. 만약 tmp가 이미 제거된 숫자라면 다시 다음 숫자를 pop
                    if num_count[tmp] == 0:
                        continue
                    # 3.3. 아직 제거되지 않았다면
                    else:
                        # 3.4. 해당 숫자 개수를 1 감소, 힙에 들어있는 숫자 개수를 1 감소시키고 break
                        num_count[tmp] -= 1
                        cnt -= 1
                        break
            # 4. 최솟값을 찾아서 삭제하는 연산일 경우
            else:
                while True:
                    # 4.1. 힙에서 최솟값을 뽑아서 tmp에 저장하고
                    tmp = heappop(min_heap)
                    # 4.2. 만약 tmp가 이미 제거된 숫자가 아니라면 다시 다음 숫자를 pop
                    if num_count[tmp] == 0:
                        continue
                    # 4.3. 아직 제거되지 않았다면
                    else:
                        # 4.4. 해당 숫자 개수를 1 감소, 힙에 들어있는 숫자 개수를 1 감소시키고 break
                        num_count[tmp] -= 1
                        cnt -= 1
                        break

    # 5. 힙이 비어있지 않다면
    if cnt != 0:
        min_num = math.inf
        max_num = -math.inf
        # 5.1. 개수가 남아있는 숫자가 나올 때까지 최댓값을 계속 pop
        while max_heap:
            tmp_num = -heappop(max_heap)
            if num_count[tmp_num] != 0:
                max_num = tmp_num
                break
        # 5.2. 개수가 남아있는 숫자가 나올 때까지 최솟값을 계속 pop
        while min_heap:
            tmp_num = heappop(min_heap)
            if num_count[tmp_num] != 0:
                min_num = tmp_num
                break

        print(max_num, min_num)
    else:
        print('EMPTY')
