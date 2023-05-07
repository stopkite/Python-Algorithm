def solution(s):
    answer = []
    temp = []
    for i in range(len(s)):
        if s[i] not in temp:
            temp.append(s[i])
            answer.append(-1)
        else:
            max_idx = 0
            for j in range(i):
                if s[j] == s[i]:
                    if j > max_idx:
                        max_idx = j
            answer.append(i - max_idx)
    return answer