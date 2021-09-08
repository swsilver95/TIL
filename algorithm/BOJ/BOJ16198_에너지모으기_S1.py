N = int(input())
marbles = list(map(int, input().split()))
sel_list = []
for b in range(1, 9):
    for c in range(1, 8):
        for d in range(1, 7):
            for e in range(1, 6):
                for f in range(1, 5):
                    for g in range(1, 4):
                        for h in range(1, 3):
                            for i in range(1, 2):
                                sel_list.append([b, c, d, e, f, g, h, i])

max_energy = 0
for select in sel_list:
    idx_select = select[10 - N:]
    marbles_copy = marbles[:]
    energy = 0
    for j in range(N - 2):
        energy += marbles_copy[idx_select[j] - 1] * marbles_copy[idx_select[j] + 1]
        marbles_copy.pop(idx_select[j])
    if max_energy < energy:
        max_energy = energy


print(max_energy)