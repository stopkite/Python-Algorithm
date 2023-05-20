def solution(n):
    answer = n
    one_cnt = bin(n).count('1')

    while True:
        answer += 1
        answer_one_cnt = bin(answer).count('1')

        if one_cnt == answer_one_cnt:
            break

    return answer