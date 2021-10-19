def solution(leave, day, holidays):
    week = {
        'FRI': [2, 3],
        'SAT': [1, 2],
        'SUN': [0, 1],
        'MON': [6, 0],
        'TUE': [5, 6],
        'WED': [4, 5],
        'THU': [3, 4]
    }
    max_holiday = 0
    for i in range(31):
        tmp_holiday = 0
        cnt = leave
        while i <= 30 and cnt > 0:
            if i in holidays or i % 7 in week[day]:
                tmp_holiday += 1
                i += 1
            else:
                cnt -= 1
                tmp_holiday += 1
                i += 1

        if i == 30:
            if i in holidays or i % 7 in week[day]:
                tmp_holiday += 1

        # i번째는 확인한 원소가 아님
        while i < 30:
            if i in holidays or i % 7 in week[day]:
                tmp_holiday += 1
                i += 1
            else:
                break

        if max_holiday < tmp_holiday:
            max_holiday = tmp_holiday

    answer = max_holiday
    return answer


leave = 30
day = "MON"
holidays = [1, 2, 3, 4, 28, 29, 30]
print(solution(leave, day, holidays))