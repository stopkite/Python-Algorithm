def solution(n, m, section):
    answer = 1
    paint_start = section[0]
    for i in range(1, len(section)):
        if section[i] - paint_start >= m:
            answer += 1
            paint_start = section[i]
    return answer