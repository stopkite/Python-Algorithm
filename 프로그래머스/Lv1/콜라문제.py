def solution(a, b, n):
    answer = 0
    res = 0
    while n >= a:
        res = n % a
        n = (n // a) * b
        answer += n
        n += res

    return answer