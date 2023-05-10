def solution(k, score):
    answer = []
    rank = []
    for i in range(len(score)):
        rank.append(score[i])
        if i + 1 > k:
            rank.sort()
            rank.pop(0)
        answer.append(min(rank))

    return answer