def solution(array, commands):
    answer = []
    for item in commands:
        i = item[0]
        j = item[1]
        k = item[2]

        temp = array[i - 1:j]
        temp.sort()
        answer.append(temp[k - 1])

    return answer