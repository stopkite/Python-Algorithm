def solution(n):
    a = [0] * (n + 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if a[i] == 0:
            for j in range(i + i, n + 1, i):
                a[j] = 1

    answer = 0
    for i in range(2, n + 1):
        if a[i] == 0:
            answer += 1

    return answer