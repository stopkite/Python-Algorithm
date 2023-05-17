def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1] - 1
        idx = commands[i][2] - 1

        new_a = array[start: end + 1]
        new_a.sort()
        answer.append(new_a[idx])

    return answer