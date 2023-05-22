def solution(n, m, section):
    answer = 0
    temp = 0

    for i in range(len(section)):
        if section[i] <= temp:
            continue
        else:
            answer += 1
            temp = section[i] + (m - 1)

    return answer