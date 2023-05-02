def solution(s):
    s = s.upper()

    p_cnt = s.count("P")
    y_cnt = s.count("Y")

    if p_cnt == y_cnt:
        return True
    else:
        return False
