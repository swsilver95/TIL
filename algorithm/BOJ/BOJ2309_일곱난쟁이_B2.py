import sys
N = 9
numbers = [int(input()) for _ in range(N)]
sel = [0] * N


def find_seven(idx):
    if idx == N:
        total = []
        if sum(sel) == 7:
            for i in range(N):
                if sel[i]:
                    total.append(numbers[i])
            if sum(total) == 100:
                total.sort()
                for num in total:
                    print(num)
                sys.exit(0)

    else:
        sel[idx] = 1
        find_seven(idx + 1)
        sel[idx] = 0
        find_seven(idx + 1)


find_seven(0)
