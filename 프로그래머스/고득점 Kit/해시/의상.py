def solution(clothes):
    answer = 1
    cd = {}

    for c in clothes:
        if c[1] not in cd:
            cd[c[1]] = 1
        else:
            cd[c[1]] += 1

    if len(cd) == 1:
        return len(clothes)
    else:
        for k, v in cd.items():
            answer *= (v + 1)
        answer -= 1
        return answer
