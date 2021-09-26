import sys
sys.stdin = open('input.txt')

T = int(input())


def heap_push(value):
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    child = heap_count
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    heap = [0] * (N + 1)
    heap_count = 0

    for number in numbers:
        heap_push(number)

    answer = 0
    while N > 0:
        N = N // 2
        answer += heap[N]

    print('#{} {}'.format(tc, answer))
