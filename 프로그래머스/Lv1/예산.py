def solution(d, budget):
    d.sort()
    cnt = 0
    total = 0
    for money in d:

        total += money

        if budget < total:
            break

        cnt += 1

    return cnt