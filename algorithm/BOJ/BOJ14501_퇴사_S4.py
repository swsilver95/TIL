'''
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 
비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
N = 7인 경우에 다음과 같은 상담 일정표를 보자.

1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 
5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.
상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 
예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 
2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
퇴사 전에 할 수 있는 상담의 최대 이익은 
1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 
1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

입력 예시 1)
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

출력 예시 1)
45

'''
import sys
import itertools

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

dummy = list(range(1, N + 1))
my_dict = dict()
for i in range(N):
    if i + data[i][0] > N:
        continue
        # f스트링에 문제가 생겨서 임시로 주석처리
    # else:
    #     my_dict[f'{i+1}, {data[i][1]}'] = dummy[i: i + data[i][0]]
# print(my_dict)


def calc_date(data_dict):
    date_comb = [] # 모든 회의 일정의 조합
    for val in data_dict.values():
        date_comb.append(val)
    all_comb = [] # 모든 날짜 선택의 조합
    # print(date_comb)
    for i in range(1, len(date_comb) + 1):
        all_comb += list(itertools.combinations(date_comb, i))
    # print(len(date_comb))
    # print(all_comb)
    return all_comb


def validate_list(cases):
    good_list = [] # 최종 가능 케이스 모음
    for case in cases:
        tmp_set = set(case[0]) # 피벗을 케이스의 [0]번 집합으로 만듦
        base_len = len(case[0]) # 합집합하기 전의 길이
        for i in range(1, len(case)): # [0]번은 이미 피벗으로 뽑았으므로 [1]부터
            tmp_set = tmp_set | set(case[i]) #[i]번과 계속 합집합함
            base_len += len(case[i]) # 마찬가지로 나중에 비교할 길이도 저장
        # print(tmp_set)
        if len(tmp_set) < base_len: # 합집합 결과의 길이가, 합집합 전 집합들의 길이보다 작은 경우에는 중복된 값이 있었다는 뜻, continue
            continue
        else: # 만약 같으면 가능한 케이스, good_list에 추가
            good_list.append(case)
    return good_list

my_cases = calc_date(my_dict)
best_list = validate_list(my_cases)
# print(best_list)


def get_key(val):
    for key, value in my_dict.items():
         if val == value:
             return key


def money(real_list):
    max_list = []
    for k in real_list:
        # print(k)
        total = 0
        for m in range(len(k)):
            x, dollar = map(int, get_key(k[m]).split(', '))
            total += dollar
        max_list.append(total)
    # print(max_list)
    if len(max_list) != 0:
        return max(max_list)
    else:
        return 0


print(money(best_list))

'''
# 정민 코드
import sys

n = int(sys.stdin.readline())  # 퇴사 전 날을 입력 받음
data = []  # 입력 받을 배열
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))  # 입력 받기
ans = 0


def cgs(idx, value):  # 답을 찾는 재귀 함수
    if idx == n:  # 0일 부터 시작하므로 딱 n일 경우 종료
        global ans
        if ans < value:  # 최댓값을 저장함
            ans = value
        return
    if idx > n:  # 그 이상 일경우 상담 불가능
        return
    cgs(idx + data[idx][0], value + data[idx][1])  # 상담을 하는 경우 재귀
    cgs(idx + 1, value)  # 상담을 하지 않고 다음날을 가는 경우


cgs(0, 0)  # 스타토
sys.stdout.write(str(ans))  # 정답 출력
'''