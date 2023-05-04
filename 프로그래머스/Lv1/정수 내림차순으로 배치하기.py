def solution(n):
    arr = list(map(int, str(n)))
    arr.sort(reverse=True)

    arr2 = []
    for elem in arr:
        arr2.append(str(elem))

    return int(''.join(arr2))