import heapq

N, X = map(int, input().split())
presents = list(map(int, input().split()))


def is_available(line_num):
    heap = [0] * line_num
    for present in presents:
        tmp = heapq.heappop(heap) + present
        if tmp > X:
            return False
        heapq.heappush(heap, tmp)

    return True


start = 1
end = 100000
answer = 0
while start <= end:
    line_num = (start + end) // 2
    if is_available(line_num):
        end = line_num - 1
        answer = line_num
    else:
        start = line_num + 1

print(answer)
