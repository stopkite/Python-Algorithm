def solution(n):
    sum_val = 0
    for num in range(1, n + 1):
        if n % num == 0:
            sum_val += num

    return sum_val
