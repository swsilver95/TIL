def solution(registered_list, new_id):
    answer = ''
    if new_id not in registered_list:
        answer = new_id
    else:
        visited = set()
        S = ''
        N = ''
        i = 0
        while i < len(new_id):
            if new_id[i].isalpha():
                i += 1
                continue
            else:
                break

        if i == len(new_id):
            S = new_id
            N = ''
        else:
            S = new_id[:i]
            N = new_id[i:]
        S, N = new_id.split()

        for token in registered_list:
            if S not in token:
                continue
            else:
                if S == token:
                    visited.add(0)
                else:
                    n, k = token.split(S)
                    if len(k) != 0:
                        visited.add(k)

        if len(N) == 0:
            N = '0'
        while N not in visited():
            N = str(int(N) + 1)

        answer = S + N

    return answer

registered_list = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
new_id = "cow"

print(solution(registered_list, new_id))