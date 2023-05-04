def solution(a, b):
    sum_val = 0
    for elem in range(min(a, b), max(a, b) + 1):
        sum_val += elem

    return sum_val