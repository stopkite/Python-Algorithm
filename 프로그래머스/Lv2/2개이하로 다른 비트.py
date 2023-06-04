def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            num = bin(num)[2:]
            if '0' not in num:
                answer.append(int('10' + num[1:], 2))
            else:
                idx = num.rfind('0')
                answer.append(int(num[:idx] + '10' + num[idx + 2:], 2))

    return answer