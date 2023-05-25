def solution(survey, choices):
    result = ''
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    type = {'R': 0, 'T': 0,
            'C': 0, 'F': 0,
            'J': 0, 'M': 0,
            'A': 0, 'N': 0}

    for i in range(len(choices)):
        if choices[i] in range(1, 4):
            type[survey[i][0]] += score[choices[i]]
        else:
            type[survey[i][1]] += score[choices[i]]

    result += get_type(type, 'R', 'T')
    result += get_type(type, 'C', 'F')
    result += get_type(type, 'J', 'M')
    result += get_type(type, 'A', 'N')

    return result


def get_type(type, t1, t2):
    if type[t1] > type[t2]:
        return t1
    elif type[t1] < type[t2]:
        return t2
    else:
        temp = sorted([t1, t2])
        return temp[0]
