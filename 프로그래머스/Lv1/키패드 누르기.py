def solution(numbers, hand):
    answer = ''
    numbers = list(map(str, numbers))
    current_left = '*'
    current_right = '#'

    distance = {'1': [0, 0], '2': [0, 1], '3': [0, 2],
                '4': [1, 0], '5': [1, 1], '6': [1, 2],
                '7': [2, 0], '8': [2, 1], '9': [2, 2],
                '*': [3, 0], '0': [3, 1], '#': [3, 2]}

    for number in numbers:
        if number == '1' or number == '4' or number == '7':
            current_left = number
            answer += 'L'
        elif number == '3' or number == '6' or number == '9':
            current_right = number
            answer += 'R'
        else:  # 2,5,8,0
            left_distance = abs(distance[current_left][0] - distance[number][0]) + abs(
                distance[current_left][1] - distance[number][1])
            right_distance = abs(distance[current_right][0] - distance[number][0]) + abs(
                distance[current_right][1] - distance[number][1])

            if left_distance == right_distance:  # 거리가 같을 때
                if hand == "left":
                    current_left = number
                    answer += 'L'
                elif hand == "right":
                    current_right = number
                    answer += 'R'
            elif left_distance > right_distance:  # 오른쪽이 더 가까울 때
                current_right = number
                answer += 'R'
            else:  # 왼쪽이 더 가까울 때
                current_left = number
                answer += 'L'
    print(answer)
    return answer
