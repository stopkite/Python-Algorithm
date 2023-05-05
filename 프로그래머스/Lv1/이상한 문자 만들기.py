def solution(s):
    answer = ''
    idx = 0
    for w in s:
        if w == ' ':
            answer += ' '
            idx = 0
            continue

        if idx % 2 == 1:
            answer += w.lower()
        else:
            answer += w.upper()

        idx += 1

    return answer