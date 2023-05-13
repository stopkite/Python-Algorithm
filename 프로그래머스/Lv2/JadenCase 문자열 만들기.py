def solution(s):
    answer = ''
    if s[0].isalpha() == False:
        answer += s[0]
    else:
        answer += s[0].upper()

    for i in range(1, len(s)):
        if s[i - 1] == " ":
            if s[i].isalpha() == False:
                answer += s[i]
            else:
                answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer