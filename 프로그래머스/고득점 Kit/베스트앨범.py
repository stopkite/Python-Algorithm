def solution(genres, plays):
    answer = []
    pd = {}
    for i in range(len(plays)):
        if genres[i] not in pd:
            pd[genres[i]] = plays[i]
        else:
            pd[genres[i]] += plays[i]

    pd = dict(sorted(pd.items(), key=lambda x: x[1], reverse=True))

    pg = []
    for i in range(len(plays)):
        pg.append((i, genres[i], plays[i]))
    pg.sort(key=lambda x: (x[2]), reverse=True)

    for k, v in pd.items():
        cnt = 0
        for i in range(len(pg)):
            if cnt == 2:
                break

            if k == pg[i][1]:
                answer.append(pg[i][0])
                cnt += 1

    return answer
