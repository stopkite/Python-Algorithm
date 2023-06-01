def solution(n, k):
    answer = 0
    s = get_rev_base(n, k)

    arr = s.split('0')
    print(arr)
    for i in arr:
        if len(i) > 0:
            if int(i) != 1 and is_prime_num(int(i)):
                answer += 1
    return answer


def get_rev_base(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime_num(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
