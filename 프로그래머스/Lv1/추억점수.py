def solution(name, yearning, photo):
    yearn_dict = {}
    for i in range(len(name)):
        yearn_dict[name[i]] = yearning[i]

    answer = []
    for items in photo:
        temp = []
        for item in items:
            for k, v in yearn_dict.items():
                if k == item:
                    temp.append(v)
        answer.append(sum(temp))
    return answer