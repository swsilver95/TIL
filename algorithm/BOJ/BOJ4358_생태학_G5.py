import sys
from collections import defaultdict, OrderedDict
input = sys.stdin.readline
trees = defaultdict(int)
cnt = 0

for _ in range(1000001):
    tree = input().strip()
    if not tree:
        break
    cnt += 1
    trees[tree] += 1


sorted_trees = OrderedDict(sorted(trees.items(), key=lambda x: x[0]))

for tree, value in sorted_trees.items():
    ratio = round((value / cnt) * 100, 4)
    print(tree, '{:.4f}'.format(ratio))
