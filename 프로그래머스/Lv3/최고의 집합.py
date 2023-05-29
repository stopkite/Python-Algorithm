def solution(n, s):
    answer = []
    if s // n == 0:
        return [-1]

    while n > 0:
        answer.append(s // n)
        s -= s // n
        n -= 1

    return answer