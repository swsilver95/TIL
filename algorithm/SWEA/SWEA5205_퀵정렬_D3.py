'''
T = int(input())


def quick_sort(arr):
    # 만약 arr의 길이가 1 이하라면 arr을 그대로 리턴
    if len(arr) <= 1:
        return arr

    # 피벗 값은 어딜 잡아도 상관이 없으나, 보편적으로 가운데 값을 선정
    pivot = arr[len(arr) // 2]

    # 피벗보다 작은 값이 들어갈 리스트 left, 피벗과 같은 값이 들어갈 리스트 center, 피벗보다 큰 값이 들어갈 리스트 right를 초기화
    left = []
    center = []
    right = []
    # arr의 원소들 num에 대해서 각각 처리
    for num in arr:
        # 숫자가 피벗보다 작다면 left에 추가
        if num < pivot:
            left.append(num)
        # 숫자가 피벗보다 크다면 right에 추가
        elif num > pivot:
            right.append(num)
        # 같다면 center에 추가
        else:
            center.append(num)
    # 분할된 각 리스트를 합쳐주되, 값이 같은 center 배열은 가운데에 합연산으로 추가
    # 분할 정복
    return quick_sort(left) + center + quick_sort(right)


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = quick_sort(numbers)
    print('#{} {}'.format(tc, answer[N // 2]))
'''
def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = quick_sort(nums, 0, len(nums)-1)
    print('#{} {}'.format(tc, sorted_nums[N//2]))
