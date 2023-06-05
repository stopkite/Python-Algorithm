def solution(order):
    temp = []
    num = 1
    cur = 0

    while num != len(order) + 1:
        temp.append(num)
        while temp[-1] == order[cur]:
            cur += 1
            temp.pop()

            if len(temp) == 0:
                break
        num += 1

    return cur
