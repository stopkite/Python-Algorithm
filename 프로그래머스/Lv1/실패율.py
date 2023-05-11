def solution(N, stages):
    total = len(stages)
    fail_percent = []
    fail_user = [0]
    for stage in range(1, N + 1):
        cnt = 0
        for i in range(len(stages)):
            if stages[i] == stage:
                cnt += 1
        fail_user.append(cnt)
        total -= fail_user[stage - 1]
        if cnt == 0:
            fail_percent.append([stage, 0])
        else:
            fail_percent.append([stage, cnt / total])

    fail_percent.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for i in range(len(fail_percent)):
        answer.append(fail_percent[i][0])

    return answer