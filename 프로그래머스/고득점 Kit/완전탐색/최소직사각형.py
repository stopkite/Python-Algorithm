def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):  # 가로, 세로 중 긴 값을 가로에 넣는다
        if sizes[i][0] > sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            w.append(sizes[i][1])
            h.append(sizes[i][0])

    answer = max(w) * max(h)  # 가로, 세로 배열에 들어있는 값 중 큰 값을 곱해준다

    return answer
