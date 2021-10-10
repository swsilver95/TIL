N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))


def count_trees(height):
    length = 0
    for tree in trees:
        if tree > height:
            length += tree - height

    if length >= M:
        return True
    else:
        return False


def binary_search():
    global answer
    start = 1
    end = trees[-1]

    while start <= end:
        h = (start + end) // 2
        if count_trees(h):
            answer = h
            start = h + 1
        else:
            end = h - 1


answer = 0
binary_search()
print(answer)
