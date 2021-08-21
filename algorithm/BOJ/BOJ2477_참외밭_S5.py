K = int(input())

'''
동 1
서 2
남 3
북 4
'''
d_list = []
n_list = []
width = []
height = []
for _ in range(6):
    d, n = map(int, input().split())
    d_list.append(d)
    n_list.append(n)
    if d == 1 or d == 2:
        width.append(n)
    else:
        height.append(n)

d_cycle = ''.join(map(str, d_list * 2))
# print(d_cycle)
n_cycle = n_list * 2

'''
┐ 3131
┘ 2323
└ 4242
┌ 1414
'''
cases = ['3131', '2323', '4242', '1414']
base_area = max(width) * max(height)
for case in cases:
    if case in d_cycle:
        # print(case, 'case')
        idx = d_cycle.find(case)
        # print(idx)
        sub_area = n_cycle[idx + 1] * n_cycle[idx + 2]

print(K * (base_area - sub_area))
