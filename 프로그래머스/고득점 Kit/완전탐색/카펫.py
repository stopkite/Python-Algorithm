def solution(brown, yellow):
    total = brown + yellow
    for num in range(3, total + 1):
        if total % num == 0:
            w = num
            h = total // num

            if (w - 2) * (h - 2) == yellow:
                answer = [h, w]
                break

    return answer