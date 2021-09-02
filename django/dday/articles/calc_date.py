import datetime
from pprint import pprint

def dday(start):
    # 2021-09-01
    Y, m, d = map(str, start.split('-'))
    today = datetime.date.today()
    startday = datetime.date(int(Y), int(m), int(d))
    far = (today - startday).days + 1
    from_dday = '오늘은 {}일 째 되는 날'.format(far)
    day100 = startday + datetime.timedelta(days=99)
    day200 = startday + datetime.timedelta(days=199)
    day300 = startday + datetime.timedelta(days=299)
    day400 = startday + datetime.timedelta(days=399)
    day500 = startday + datetime.timedelta(days=499)
    day600 = startday + datetime.timedelta(days=599)
    day700 = startday + datetime.timedelta(days=699)
    day800 = startday + datetime.timedelta(days=799)
    day900 = startday + datetime.timedelta(days=899)
    day1000 = startday + datetime.timedelta(days=999)
    dday_list = [day100, day200, day300, day400, day500, day600, day700, day800, day900, day1000]
    week = ['월', '화', '수', '목', '금', '토', '일']

    result = {
        'from_dday': from_dday,
    }
    tmp = 0
    for i in dday_list:
        tmp += 100
        tmp_dday = 'D+{} : {}년 {}월 {}일 {}요일'.format(tmp, i.year, i.month, i.day, week[int(i.weekday())])
        result['day{}'.format(tmp)] = tmp_dday

    return result