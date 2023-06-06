s = list(input())
answer = ''
temp = ''
tag_flag = False
for i in range(len(s)):
    if s[i] == '<':
        if temp:
            answer += temp[::-1]
            temp = ''
        answer += '<'
        tag_flag = True
    elif s[i] == '>':
        answer += '>'
        tag_flag = False
    elif s[i] == ' ':
        answer += temp[::-1]
        answer += s[i]
        temp = ''
    else:
        if tag_flag:
            answer += s[i]
        else:
            temp += s[i]

if temp:
    answer += temp[::-1]

print(answer)
