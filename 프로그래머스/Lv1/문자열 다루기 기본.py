def solution(s):
    answer = True
    for a in s:
        if a.isdigit() == False:
            answer = False
            break

    if not (len(s) == 4 or len(s) == 6):
        answer = False
    return answer
