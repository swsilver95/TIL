dx = [-1, 0, 1, 0] # 상 우 하 좌
dy = [0, 1, 0, -1]


'''
left
0 - 3
1 - 0
2 - 1
3 - 2
'''
def left_turn(r):
    r = (r + 3) % 4
    return r


'''
right
0 - 1
1 - 2
2 - 3
3 - 0
'''
def right_turn(r):
    r = (r + 1) % 4
    return r


def solution(grid):
    col = len(grid[0])
    row = len(grid)
    answer = []
    cycle = []
    for r in range(0, 4):
        x = 0
        y = 0
        initial_r = r
        cnt = 0
        tmp_cycle = []
        flag = True
        while flag:
            if cnt > 1000000:
                break

            if cnt != 0 and x == 0 and y == 0 and r == initial_r:
                if cycle:
                    thisstr = ''.join(map(str, tmp_cycle))
                    for c in cycle:
                        tmpstr = ''.join(map(str, c))
                        if len(tmpstr) == len(thisstr):
                            if thisstr in tmpstr * 2:
                                flag = False
                                break
                            else:
                                pass
                        else:
                            pass
                    else:
                        answer.append(cnt)
                        cycle.append(tmp_cycle)
                        # print(tmp_cycle)
                        break
                else:
                    answer.append(cnt)
                    cycle.append(tmp_cycle)
                    # print(tmp_cycle)
                    break

            nx = x + dx[r]
            ny = y + dy[r]
            # print(nx, ny)
            if nx < 0:
                nx += row
            elif nx >= row:
                nx -= row

            if ny < 0:
                ny += col
            elif ny >= col:
                ny -= col

            tmp_cycle.append((r, nx, ny))
            if grid[nx][ny] == 'S':
                x, y = nx, ny
                cnt += 1
                continue

            elif grid[nx][ny] == 'L':
                r = left_turn(r)
                x, y = nx, ny
                cnt += 1
                continue

            elif grid[nx][ny] == 'R':
                r = right_turn(r)
                x, y = nx, ny
                cnt += 1
                continue

    return sorted(answer)

# a = ["R","R"]
# print(solution(a))