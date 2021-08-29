import sys

# some_id = list(map(str, sys.stdin.readline()))

some_id = sys.stdin.readline()

# def solution(new_id):
#     forbidden = ['-', '_', '.']
#     # 1단계: 모든 대문자를 소문자로 바꾼다.
#     n = len(new_id)
#     for i in range(n):
#         if new_id[i].isalpha() and new_id[i].isupper():
#             new_id[i] = new_id[i].lower()
#     # 2단계: 소문자, 숫자, -, _, .을 제외한 모든 문자를 제거
#     my_id = []
#     for i in range(n):
#         if (not new_id[i].isalpha()) and (not new_id[i].isdigit()) and (new_id[i] not in forbidden):
#             continue
#         else:
#             my_id.append(new_id[i])
#
#     # 3단계: 마침표가 연속으로 두 번 이상 사용되면 하나의 마침표로 치환
#     j = 0
#     while j < len(my_id) - 1:
#         if my_id[j] == '.':
#             if my_id[j + 1] == '.':
#                 my_id.pop(j)
#                 continue
#         j += 1
#
#     # 4-1단계: 마침표가 처음에 위치한다면 제거
#     # 이 과정에서 이미 id의 길이가 0이 될 수 있으므로 인덱스에러를 방지하고자 길이조건 사용
#     if len(my_id) >= 1:
#         if my_id[0] == '.':
#             my_id.pop(0)
#
#     # 4-2단계: 마침표가 마지막에 위치한다면 제거
#     if len(my_id) >= 1:
#         if my_id[-1] == '.':
#             my_id.pop()
#
#     # 5단계: 만약 id가 빈 문자열이면 'a' 하나를 대입
#     if len(my_id) == 0:
#         my_id.append('a')
#
#     # 6-1단계: id의 길이가 16 이상이면 15가 될때까지 마지막 문자를 제거
#     while len(my_id) >= 16:
#         my_id.pop()
#
#     # 6-2단계: 길이 맞추기 후에 마지막 문자가 . 으로 남아있으면 제거
#     # 이 과정에서는 비어있는 id가 존재할 수 없음
#     # 또한 . 이 연속으로 2개 이상 존재할 수 없음
#     if my_id[-1] == '.':
#         my_id.pop()
#
#     # 7단계: id의 길이가 2 이하라면, 아이디의 마지막 문자를 길이가 3이 될때까지 반복해서 추가
#     while len(my_id) <= 2:
#         last = my_id[-1]
#         my_id.append(last)
#
#     # 결과를 리턴
#     answer = ''.join(my_id)
#     return answer


def solution(new_id):
    forbidden = ['-', '_', '.']
    # 1단계: 모든 대문자를 소문자로 바꾼다.
    new_id = new_id.lower()

    # 2단계: 소문자, 숫자, -, _, .을 제외한 모든 문자를 제거
    for i in new_id:
        if not i.isdigit() and not i.isalpha() and i not in forbidden:
            new_id = new_id.replace(i, '')

    # 3단계: 마침표가 연속으로 두 번 이상 사용되면 하나의 마침표로 치환
    cnt = new_id.count('..')
    for _ in range(cnt):
        new_id = new_id.replace('..', '.')

    # 4단계: 마침표가 처음이나 마지막에 위치한다면 제거
    new_id = new_id.strip('.')

    # 5단계: 만약 id가 빈 문자열이면 'a' 하나를 대입
    if len(new_id) == 0:
        new_id += 'a'

    # 6-1단계: id의 길이가 16 이상이면 15가 될때까지 마지막 문자를 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]

    # 6-2단계: 길이 맞추기 후에 마지막 문자가 . 으로 남아있으면 제거
    new_id = new_id.rstrip('.')

    # 7단계: id의 길이가 2 이하라면, 아이디의 마지막 문자를 길이가 3이 될때까지 반복해서 추가
    while len(new_id) <= 2:
        last = new_id[-1]
        new_id += last

    # 결과를 리턴
    answer = ''.join(new_id)
    return answer
