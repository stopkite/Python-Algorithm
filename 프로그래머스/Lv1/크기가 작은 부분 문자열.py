def solution(t, p):
    answer = 0
    temp = []
    for i in range(len(t) - len(p) + 1):
        temp.append(int(t[i:i + len(p)]))

    cnt = 0

    for i in range(len(temp)):
        if temp[i] <= int(p):
            cnt += 1

    return cnt