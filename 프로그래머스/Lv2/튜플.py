'''
문자열 split으로 항상 문자를 하나씩 잘랐는데,
},{ 같이 한번에 여러개를 기준으로 자를 수 있다는 것을 처음 배웠다.
'''
def solution(s):
    answer = []
    s = s[2:len(s) - 2]
    s = s.split("},{")
    s.sort(key=len)

    for i in s:
        temp = i.split(',')
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))

    return answer