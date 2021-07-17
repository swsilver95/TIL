'''
https://www.acmicpc.net/problem/10799
'''

data = input()

# 문자열 일부 치환 / ()를 0으로 바꿈
data_rep = data.replace("()", "0")

# "("의 개수를 셈
num = data_rep.count("(")

# 문자열 앞에서부터 "("를 각각 1, 2, 3, ... 으로 치환
# 이 때 치환한 개수는 최종적으로 count - 1개
count = 1
for i in range(len(data_rep)):
    if data_rep[i] == "(":
        data_rep = data_rep.replace("(", str(count), 1)
        count += 1

# ")" 역시 숫자로 치환해 주는 함수 구성
def replace_right(x):
    # 체크를 위한 리스트 생성, 입력 스트링을 똑같이 복제
    x_check = x
    j = 0
    while j < len(x):
        # 0인 부분은 그냥 스킵
        if x_check[j] == "0":
            j = j + 1
            continue
        
        # x_check 지점에 ")"가 있으면, 동일 지점의 x를 tmp로 치환
        # 막대가 생성되면 x_check에서 막대가 생성된 위치를 모두 0으로 변경
        if x_check[j] == ")":
            x = x.replace(")", str(tmp), 1)
            x_check = x_check.replace(")", str(tmp), 1)
            x_check = x_check.replace(str(tmp), "0")
            j = 0 # 다시 처음부터 시작할 수 있도록 j를 초기화
        
        # x_check가 0이 아니라면, 해당 위치의 숫자를 tmp로 등록
        if x_check[j] != "0":
            tmp = x_check[j]
            j = j + 1

    return(x)        
    
# 막대 개수를 세는 함수
def count_stick(y):
    global count 
    stick_num = 0
    for i in range(1, count):
        num1 = y.find(str(i), 0) # i값이 리스트 앞에서부터 몇 번째 인덱스인지 찾음
        num2 = y.rfind(str(i), 1) + 1 # 마찬가지로 뒤에서부터 찾음
        stick_num += y[num1 : num2].count("0") + 1 # 슬라이싱해서 레이저의 개수를 셈
    return(stick_num)
        

data_stick = replace_right(data_rep)
print(count_stick(data_stick))
