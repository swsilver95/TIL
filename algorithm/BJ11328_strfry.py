import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(list(map(str, input().rstrip().split(' '))))

def strfry(my_strings):
    alphabet_cnt = [0] * 26
    word1 = list(map(str, my_strings[0]))
    word2 = list(map(str, my_strings[1]))

    for i in word1:
        alphabet_cnt[ord(i) - 97] += 1
        # print(alphabet_cnt)
    for j in word2:
        alphabet_cnt[ord(j) - 97] -= 1
        # print(alphabet_cnt)
    
    if any(alphabet_cnt):
        return 'Impossible'
    return 'Possible'

for word in words:
    print(strfry(word))
