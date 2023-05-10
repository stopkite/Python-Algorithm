def solution(k, m, score):
    result = 0

    score.sort(reverse=True)
    min_val = k

    for i in range(len(score)):
        if min_val > score[i]:
            min_val = score[i]

        if (i + 1) % m == 0:
            result += min_val * m
    return result