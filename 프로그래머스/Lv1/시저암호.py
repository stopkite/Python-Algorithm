def solution(s, n):
    answer = ''
    for w in s:
        if w == ' ':
            answer += ' '
        else:
            if w >= 'a' and w <= 'z':
                answer += chr((ord(w) - ord('a') + n) % 26 + ord('a'))
            elif w >= 'A' and w <= 'Z':
                answer += chr((ord(w) - ord('A') + n) % 26 + ord('A'))
    return answer
