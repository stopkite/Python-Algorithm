def solution(s):
    answer = 0

    s = list(s)
    same_cnt = 0
    diff_cnt = 0
    first_word = ''

    for x in s:
        if first_word == '':
            first_word = x
            same_cnt += 1
            continue

        if x == first_word:
            same_cnt += 1
        else:
            diff_cnt += 1

        if same_cnt == diff_cnt:
            answer += 1
            same_cnt = 0
            diff_cnt = 0
            first_word = ''

    if len(first_word) != 0:
        answer += 1

    return answer
