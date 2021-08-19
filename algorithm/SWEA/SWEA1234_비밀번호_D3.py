import sys

sys.stdin = open('input.txt')


def remove_rep(words):                          # 반복문자를 제거하는 함수
    if len(words) <= 1:                         # 길이가 1 이하인 문자를 넣었다면 문자 길이를 바로 리턴
        return words

    i = 0                                       # 조사할 첫 번째 인덱스
    while True:
        if words[i] == words[i + 1]:            # 1. 만약 조사하는 인덱스와 그 다음 인덱스에 위치한 문자가 같다면
            words = words[:i] + words[i + 2:]   # 해당 두 문자를 빼버린 문자열을 다시 만들고
            # print(words, i, '--')
            if i >= 1:                          # i가 1 이상이라면
                i -= 1                          # 1을 빼줘서 이전 문자부터 다시 조사하게 만들고 (ex. ABBA)
                if i == len(words) - 1:         # 1을 뺐더니 문자열 길이와 같아졌다면
                    break                       # 조사가 끝났다는 뜻이므로 break
        else:                                   # 2. 만약 다음 인덱스에 위치한 문자와 서로 다르다면
            i += 1                              # 다음 인덱스를 조사할 수 있게 i에 1을 더해주고
            if i == len(words) - 1:             # 마찬가지로 i가 문자열의 길이와 같아졌다면
                break                           # 조사가 끝났다는 뜻이므로 break

    return words


for tc in range(1, 11):
    N, pw = map(str, input().split())
    print('#{} {}'.format(tc, remove_rep(pw)))