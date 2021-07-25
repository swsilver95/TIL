N = int(input())
numbers = list(map(int, str(N)))
# print(numbers)

card = 0 # 세트 개수 변수 설정
cnt_list = [0] * 10 # 각 숫자별 잔여량을 나타낼 리스트
for number in numbers:
    if number == 6 or number == 9:
        if cnt_list[6] == 0 and cnt_list[9] == 0:
            card += 1
            cnt_list = [x+1 for x in cnt_list]
            cnt_list[number] -= 1
            # print(cnt_list)
        elif cnt_list[6] == 0 and cnt_list[9] != 0:
            cnt_list[9] -= 1
        elif cnt_list[6] != 0 and cnt_list[9] == 0:
            cnt_list[6] -= 1
        elif cnt_list[6] != 0 and cnt_list[9] != 0:
            cnt_list[6] -= 1
    else:
        if cnt_list[number] == 0: # 리스트 내에 카드 잔여량이 없으면
            card += 1 # 세트를 한개 구매해서
            cnt_list = [x+1 for x in cnt_list] # 리스트에 카드가 전부 다 하나씩 늘어나고
            cnt_list[number] -= 1 # 한 장은 사용함
        elif cnt_list[number] > 0: # 아직 남은 카드가 있다면
            cnt_list[number] -= 1 # 마찬가지로 한 장 사용함
    
print(card)
