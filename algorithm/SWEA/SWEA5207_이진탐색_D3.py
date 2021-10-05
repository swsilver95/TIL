T = int(input())


# def binary_search(left, right, t):
#     global cnt
#
#     mid = (left + right) // 2
#     m = numbers[mid]
#     print(m)
#
#     if t == m:
#         cnt += 1
#         return
#     elif m > t:
#         binary_search(left, mid + 1, t)
#     elif m < t:
#         binary_search(mid + 1, right, t)
#     else:
#         return


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    targets = list(map(int, input().split()))
    cnt = 0

    for target in targets:
        left = 0
        right = N - 1
        flag = 0

        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                cnt += 1
                break
            elif numbers[mid] > target:
                right = mid - 1
                if flag == 1:
                    break
                flag = 1
            elif numbers[mid] < target:
                left = mid + 1
                if flag == -1:
                    break
                flag = -1

    print('#{} {}'.format(tc, cnt))