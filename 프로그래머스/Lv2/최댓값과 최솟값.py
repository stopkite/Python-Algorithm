def solution(s):
    arr = list(map(int, s.split(" ")))
    min_val = str(min(arr))
    max_val = str(max(arr))
    answer = min_val + " " + max_val
    return answer