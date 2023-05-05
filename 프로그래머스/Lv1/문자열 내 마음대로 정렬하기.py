def solution(strings, n):
    temp = []
    for word in strings:
        temp.append(word[n] + word)

    temp.sort()

    answer = []
    for word in temp:
        answer.append(word[1:])

    return answer