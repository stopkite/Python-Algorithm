def solution(participant, completion):
    answer = []
    p = {}
    for elem in participant:
        if elem not in p:
            p[elem] = 1
        else:
            p[elem] += 1

    for elem in completion:
        p[elem] -= 1

    for k, v in p.items():
        if p[k] == 1:
            answer = k

    return answer