from collections import defaultdict


def solution(id_list, k):
    coupons = defaultdict(int)
    for d in id_list:
        ids = list(map(str, d.split()))
        ids = set(ids)
        for id in ids:
            if coupons[id] < k:
                coupons[id] += 1

    answer = 0
    for id, coupon in coupons.items():
        answer += coupon

    return answer


print(solution(["A B C D", "A D", "A B D", "B D"], 2))