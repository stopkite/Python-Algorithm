from collections import Counter


def solution(want, number, discount):
    answer = 0
    w_dict = {}
    for i in range(len(want)):
        w_dict[want[i]] = number[i]

    d = []
    for i in range(len(discount) - 9):
        d.append(discount[i:10 + i])

    w_dict = dict(sorted(w_dict.items()))
    for items in d:
        c_dict = dict(sorted(dict(Counter(items)).items()))
        if w_dict == c_dict:
            answer += 1

    return answer