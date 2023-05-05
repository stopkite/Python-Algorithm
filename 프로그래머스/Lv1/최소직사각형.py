def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(min(sizes[i]))
        h.append(max(sizes[i]))

    max_w = max(w)
    max_h = max(h)

    answer = max_w * max_h
    return answer
