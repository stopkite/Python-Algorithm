def solution(info, query):
    answer = []
    q = []
    for i in range(len(query)):  # query 정보 담기
        query[i] = query[i].replace(" and", "")
        q.append(query[i].split(' '))

    user_info = {}  # 유저 정보 담기
    for idx, i in enumerate(info):
        user_info[idx] = i.split()

    for c in q:
        cnt1 = []
        cnt2 = []
        cnt3 = []
        cnt4 = []
        cnt5 = []

        for k, v in user_info.items():
            if c[0] != '-':
                if v[0] == c[0]:
                    cnt1.append(k)
            else:
                cnt1.append(k)

            if c[1] != '-':
                if v[1] == c[1]:
                    cnt2.append(k)
            else:
                cnt2.append(k)

            if c[2] != '-':
                if v[2] == c[2]:
                    cnt3.append(k)
            else:
                cnt3.append(k)

            if c[3] != '-':
                if v[3] == c[3]:
                    cnt4.append(k)
            else:
                cnt4.append(k)

            if c[4] != '-':
                if int(v[4]) >= int(c[4]):
                    cnt5.append(k)
            else:
                cnt5.append(k)
        total = len(set(cnt1) & set(cnt2) & set(cnt3) & set(cnt4) & set(cnt5))
        answer.append(total)

    return answer
