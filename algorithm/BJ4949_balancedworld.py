sentences = []
while True:
    s = input()
    if s != '.':
        sentences.append(s)
    else:
        break
# print(sentences)

def jeongmin(blah):
    if blah == '.':
        return 'yes'
    blah_list = []
    for i in blah:
        blah_list.append(i) # 문자열 다 쪼개서 리스트로 저장
    # print(blah_list)
    target = '[()]' # 서치할 괄호 목록
    stk = []
    while len(blah_list) > 0: # 문장이 다 파괴될 때까지
        if blah_list[-1] not in target: # 리스트의 마지막 값이 괄호가 아니면
            blah_list.pop() # 조져버림
        else: # 리스트의 마지막 값이 괄호라면
            if blah_list[-1] == ')' or blah_list[-1] == ']': # 만난 괄호가 )나 ]라면
                stk.append(blah_list.pop()) # 스택에 추가
            else:
                if len(stk) == 0: # 스택의 길이가 0인 상태에서 (나 [를 만나면 no 반환
                    return 'no'
                elif blah_list[-1] == '(': # 스택의 길이가 0이 아닌데 (를 만나면
                    if stk[-1] == ']': # 스택의 마지막값이 ]일때 no 반환
                        return 'no'
                    else: # 스택의 마지막값이 ) 라면
                        stk.pop() 
                        blah_list.pop() # 스택과 문장의 끝에서 하나씩 제거
                elif blah_list[-1] == '[': # 스택의 길이가 0이 아닌데 [를 만나면
                    if stk[-1] == ')': # 스택의 마지막값이 )일때 no 반환
                        return 'no'
                    else: # 스택의 마지막값이 ] 라면
                        stk.pop()
                        blah_list.pop() # 스택과 문장의 끝에서 하나씩 제거
    if len(stk) != 0:
        return 'no'
    return 'yes'

for sentence in sentences:
    print(jeongmin(sentence))