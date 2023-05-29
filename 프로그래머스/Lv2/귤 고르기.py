def solution(k, tangerine):
    answer = 0
    dic = {}

    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1

    box = sorted(list(dic.values()), reverse=True)
    for b in box:
        k = k - b
        answer += 1

        if k <= 0:
            break

    return answer