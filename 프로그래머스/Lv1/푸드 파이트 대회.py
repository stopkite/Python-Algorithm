def solution(food):
    front = ''
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            front += str(i) * ((food[i] - 1) // 2)
        else:
            front += str(i) * (food[i] // 2)

    end = '0'
    for i in front[::-1]:
        end += i

    answer = front + end

    return answer