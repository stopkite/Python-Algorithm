def solution(new_id):
    id1 = step1(new_id)
    id2 = step2(id1)
    id3 = step3(id2)
    id4 = step4(id3)
    id5 = step5(id4)
    id6 = step6(id5)
    id7 = step7(id6)

    result = id7

    return result


def step1(id):
    return id.lower()


def step2(id):
    answer = ''
    for w in id:
        if w.isalpha() or w.isnumeric() or w in '-_.':
            answer += w
    return answer


def step3(id):
    while '..' in id:
        id = id.replace("..", ".")
    return id


def step4(id):
    id = list(id)
    if len(id) >= 1:
        if id[0] == '.':
            id[0] = ''

    if len(id) >= 1:
        if id[-1] == '.':
            id[-1] = ''

    return ''.join(id)


def step5(id):
    if len(id) == 0:
        return 'a'
    else:
        return id


def step6(id):
    id = list(id)
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = id[:14]
    else:
        return ''.join(id)
    return ''.join(id)


def step7(id):
    if len(id) <= 2:
        id = id + id[-1] * (3 - len(id))
    return id
