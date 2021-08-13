import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))

    light = 0
    for i in range(2, len(buildings) - 2):
        left = max(buildings[i-2], buildings[i-1])          # 왼쪽 두 빌딩 중에서 큰 빌딩의 높이
        right = max(buildings[i+2], buildings[i+1])         # 오른쪽 두 빌딩 중에서 큰 빌딩의 높이

        if buildings[i] < left or buildings[i] < right:     # 만약 양쪽 2칸 이내에 더 높은 빌딩이 있다면
            continue                                        # 다음 빌딩을 찾으러
        else:
            light += min(buildings[i] - left, buildings[i] - right)     # 조망층의 개수를 light에 더함

    print('#{0} {1}'.format(idx, light))                                # 출력(정답확인 완료)