def solution(id_list, report, k):
    report_from_dict = {}  # key: 신고당한 사람, value: 신고한 사람
    report_to_dict = {}  # key: 신고한 사람, value: key가 신고한 사람
    for id in id_list:
        report_to_dict[id] = set()
        report_from_dict[id] = set()

    for r in report:
        a, b = r.split()
        if a != b:  # 자기 자신을 신고 하는 경우 제외
            report_to_dict[a].add(b)
            report_from_dict[b].add(a)

    stopped_id = []
    for key, value in report_from_dict.items():
        if len(value) >= k:
            stopped_id.append(key)

    answer = []
    for value in report_to_dict.values():
        cnt = 0
        for person in value:
            if person in stopped_id:
                cnt += 1
        answer.append(cnt)

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
