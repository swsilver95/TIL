n = int(input())

def sue(n, i):                              # 선택 숫자가 i 일 때의 수 이어가기 리스트를 반환
    result = []                             # 결과 리스트를 만들고 첫째 값, 둘째 값 추가
    result.append(n)
    result.append(i)

    p = 2                                   # 탐색을 시작할 인덱스는 2번부터
    while True:
        num = result[p-2] - result[p-1]     # 수 이어가기
        if num >= 0:
            result.append(num)
            p += 1
        else:                               # 이어가다가 음수가 나오면 break
            break
    return result                           # 결과 리스트를 반환

max_length = 0
for j in range(n, 0, -1):
    arr = sue(n, j)
    if max_length < len(arr):               # 더 긴 수 이어가기를 찾았다면
        max_length = len(arr)               # 최대 길이 갱신
        max_arr = arr                       # 그 때의 리스트를 저장
print(max_length)
print(*max_arr)