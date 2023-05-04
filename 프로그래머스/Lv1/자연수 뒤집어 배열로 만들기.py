def solution(n):
    arr = []
    for elem in str(n)[::-1]:
        arr.append(int(elem))
    return arr
