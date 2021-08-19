import sys

sys.stdin = open('input.txt', encoding='UTF8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    sentence = input()

    cnt = 0                                                 # 일치하는 문자열의 개수
    for i in range(0, len(sentence) - len(pattern) + 1):    # 마지막 인덱스에 pattern의 길이가 딱 들어가도록
        tmp = 0                                             # 길이 확인 임시변수
        for j in range(len(pattern)):                       # pattern의 길이만큼 인덱스를 더하면서
            if sentence[i + j] == pattern[j]:               # pattern과 sentence의 해당 부분이 같으면 tmp에 1 증가
                tmp += 1                                    
                if tmp == len(pattern):                     # tmp가 패턴의 길이와 같으면 탐색 성공
                    cnt += 1                                # cnt에 +1


    print('#{} {}'.format(tc, cnt))