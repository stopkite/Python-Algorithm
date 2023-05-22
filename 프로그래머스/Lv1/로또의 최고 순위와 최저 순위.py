def solution(lottos, win_nums):
    answer = []
    win_cnt = 0

    for l in lottos:  # 0을 제외하고 맞은 로또개수
        for w in win_nums:
            if l == w:
                win_nums.remove(w)
                win_cnt += 1

    answer.append(get_lotto_price(win_cnt))  # 최저 순위

    zero_cnt = lottos.count(0)
    for _ in range(zero_cnt):
        win_nums.pop()
        win_cnt += 1

    answer.append(get_lotto_price(win_cnt))

    return sorted(answer)


def get_lotto_price(win_cnt):
    if win_cnt == 6:
        price = 1
    elif win_cnt == 5:
        price = 2
    elif win_cnt == 4:
        price = 3
    elif win_cnt == 3:
        price = 4
    elif win_cnt == 2:
        price = 5
    else:
        price = 6
    return price
