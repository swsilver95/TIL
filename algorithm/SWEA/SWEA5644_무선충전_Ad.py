T = int(input())

dx = [0, 0, 1, 0, -1]  # 상우하좌 (x축)
dy = [0, -1, 0, 1, 0]


def check(position_A, position_B):
    a1, a2 = position_A
    b1, b2 = position_B
    st = [[] for _ in range(4)]

    for i in range(A):
        x, y, C, P = BCs[i]
        dist_a = abs(a1 - x) + abs(a2 - y)
        dist_b = abs(b1 - x) + abs(b2 - y)
        if dist_a <= C:
            st[0].append(True)
            st[1].append(P)
        else:
            st[0].append(False)
            st[1].append(0)

        if dist_b <= C:
            st[2].append(True)
            st[3].append(P)
        else:
            st[2].append(False)
            st[3].append(0)

    return st


def calc():
    global charge_a, charge_b
    A_power = status[1]
    B_power = status[3]

    case = []
    for i in range(A):
        for j in range(A):
            if i == j:
                if A_power[i] != 0 and B_power == 0:
                    case.append([A_power[i], 0])
                elif A_power[i] == 0 and B_power != 0:
                    case.append([0, B_power[j]])
                else:
                    case.append([A_power[i] // 2, B_power[j] // 2])
            else:
                case.append([A_power[i], B_power[j]])

    case.sort(key=lambda x: (x[0] + x[1]), reverse=True)
    charge_a += case[0][0]
    charge_b += case[0][1]

    return


for tc in range(1, T + 1):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    BCs = [list(map(int, input().split())) for _ in range(A)]
    p_A = [1, 1]
    p_B = [10, 10]
    charge_a = 0
    charge_b = 0
    status = check(p_A, p_B)
    calc()

    for j in range(M):
        p_A[0], p_A[1] = p_A[0] + dx[move_A[j]], p_A[1] + dy[move_A[j]]
        p_B[0], p_B[1] = p_B[0] + dx[move_B[j]], p_B[1] + dy[move_B[j]]

        status = check(p_A, p_B)
        calc()

    print('#{} {}'.format(tc, charge_a + charge_b))

