import sys
from itertools import product
input = sys.stdin.readline


formula = input()
left, M3 = formula.rstrip().split('=')
M1, M2 = left.rstrip().split('+')
# print(M1, M2, M3)


def count_atoms(x):
    n = len(x)
    my_dict = {
        'C': 0,
        'H': 0,
        'O': 0
    }
    for i in range(n):
        if x[i] in ['C', 'H', 'O']:
            if i + 1 == n:
                my_dict[x[i]] += 1
                break
            elif x[i + 1].isalpha():
                my_dict[x[i]] += 1
            elif x[i + 1].isdigit():
                my_dict[x[i]] += int(x[i + 1])

    return my_dict


m1_dict = count_atoms(M1)
m2_dict = count_atoms(M2)
m3_dict = count_atoms(M3)
# print(m1_dict)
# print(m2_dict)
# print(m3_dict)

coefficient = list(range(1, 11))
cases = list(product(coefficient, repeat=3))
# print(cases)

possible = []
for case in cases:
    a, b, c = case
    for atom in ['C', 'H', 'O']:
        if a * m1_dict[atom] + b * m2_dict[atom] == c * m3_dict[atom]:
            pass
        else:
            break
    else:
        possible.append(case)

possible.sort(key=lambda x: x[0])
print(*possible[0])
