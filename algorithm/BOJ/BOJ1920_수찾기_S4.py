N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))


def binary_search(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return 1

        if numbers[mid] < target:
            start = mid + 1

        elif numbers[mid] > target:
            end = mid - 1

    return 0


for target in targets:
    print(binary_search(target))