def solution():
    budget = int(input())
    moneys = list(map(int, input().split()))

    jun_hyun = bnp(budget, moneys)
    sung_min = timing(budget, moneys)


    if jun_hyun > sung_min:
        return "BNP"
    elif jun_hyun < sung_min:
        return "TIMING"
    else:
        return "SAMESAME"


def bnp(budget, moneys):
    cnt = 0
    for i in range(len(moneys)):
        if budget > 0 and moneys[i] <= budget:
            cnt += budget // moneys[i]
            budget -= (cnt * moneys[i])

    return budget + (cnt * moneys[-1])


def timing(budget, moneys):
    cnt = 0
    up, down = 0, 0
    for i in range(1, len(moneys)):
        if moneys[i - 1] < moneys[i]:
            down = 0
            up += 1
            if up >= 3:
                budget += moneys[i] * cnt
                cnt = 0
        elif moneys[i - 1] > moneys[i]:
            up = 0
            down += 1
            if down >= 3:
                cnt += budget // moneys[i]
                budget -= (budget // moneys[i]) * moneys[i]
        elif moneys[i - 1] == moneys[i]:
            up = 0
            down = 0

    return budget + (cnt * moneys[-1])


print(solution())
