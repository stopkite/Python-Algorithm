def solution(s, skip, index):
    s = list(s)
    skip = list(skip)
    for i in range(len(s)):
        cnt = 0
        while cnt != index:
            cnt += 1
            next_alpha = chr(ord(s[i]) + 1)
            if ord(next_alpha) > ord('z'):
                s[i] = 'a'
            else:
                s[i] = next_alpha

            if s[i] in skip:
                cnt -= 1

    answer = ''.join(s)
    return answer
