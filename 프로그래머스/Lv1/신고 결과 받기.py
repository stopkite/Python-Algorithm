def solution(id_list, report, k):
    answer = []
    report = set(list(report))

    r_dict = {}
    for r in report:
        r = r.split()
        r_dict[r[0]] = []

    for r in report:
        r = r.split()
        r_dict[r[0]].append(r[1])

    r_cnt = {}
    for r in report:
        r = r.split()
        if r[1] not in r_cnt:
            r_cnt[r[1]] = 1
        else:
            r_cnt[r[1]] += 1

    report_id_list = []
    for id, cnt in r_cnt.items():
        if cnt >= k:
            report_id_list.append(id)

    id_dict = {}
    for id in id_list:
        id_dict[id] = 0

    for id in report_id_list:
        for key, v in r_dict.items():
            if id in v:
                id_dict[key] += 1

    for v in id_dict.values():
        answer.append(v)

    return answer
