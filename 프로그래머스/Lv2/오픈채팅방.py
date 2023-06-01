def solution(record):
    order = []
    id_dict = {}
    for r in record:
        r = r.split()

        if r[0] == 'Enter':
            id_dict[r[1]] = r[2]
            order.append(('E', r[1]))
        elif r[0] == 'Leave':
            order.append(('L', r[1]))
        else:
            id_dict[r[1]] = r[2]

    answer = []
    for o in order:
        alert = ''
        nick_name = id_dict[o[1]]

        alert += nick_name

        if o[0] == 'E':
            alert += "님이 들어왔습니다."
        else:
            alert += "님이 나갔습니다."

        answer.append(alert)

    return answer