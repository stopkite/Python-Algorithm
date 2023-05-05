def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    for i in range(max(n, m), (m * n) + 1):
        if i % m == 0 and i % n == 0:
            answer.append(i)
            break

    return answer