T = int(input())


def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        cnt += 1

    merged_arr = []
    L = R = 0
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            merged_arr.append(left[L])
            L += 1
        else:
            merged_arr.append(right[R])
            R += 1
    merged_arr += left[L:]
    merged_arr += right[R:]
    return merged_arr


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    answer = merge_sort(numbers)
    print('#{} {} {}'.format(tc, answer[N//2], cnt))