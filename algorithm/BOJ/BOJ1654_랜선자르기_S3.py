K, N = map(int, input().split())

lans = []
for _ in range(K):
    tmp = int(input())
    lans.append(tmp)


def cutting(num):
    cnt = 0
    for lan in lans:
        cnt += lan // num

    if cnt >= N:
        return True
    else:
        return False


def binary_search():
    global answer
    start = 1
    end = 2147483647

    while start <= end:
        mid = (start + end) // 2
        flag = cutting(mid)
        if flag:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


answer = 0
binary_search()
print(answer)

