def solution(x):
    sum_val = sum(list(map(int,str(x))))
    if x % sum_val == 0:
        answer = True
    else:
        answer = False
    return answer