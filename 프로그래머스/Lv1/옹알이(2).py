def solution(babbling):
    answer = 0
    able = ['aya', 'ye', 'woo', 'ma']
    for i in range(len(babbling)):
        for a in able:
            if a + a in babbling[i]:
                continue
            else:
                babbling[i] = babbling[i].replace(a, ' ')

        if len(babbling[i].strip()) == 0:
            answer += 1

    return answer

