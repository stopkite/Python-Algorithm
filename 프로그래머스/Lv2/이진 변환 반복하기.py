def solution(s):
    change_cnt = 0
    zero_cnt = 0

    while s != "1":
        change_cnt += 1
        zero_cnt += s.count("0")

        one_cnt = s.count("1")
        s = bin(int(one_cnt))[2:]

    answer = [change_cnt, zero_cnt]

    return answer