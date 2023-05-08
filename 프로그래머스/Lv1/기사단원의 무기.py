def solution(number, limit, power):
    arr1 = []
    for i in range(1, number + 1):
        arr1.append(i)

    arr2 = []
    for num in arr1:
        cnt = 0
        for x in range(1, int(num ** 0.5) + 1):
            if num % x == 0:
                cnt += 1
                if x != num // x:
                    cnt += 1
        arr2.append(cnt)

    result = 0
    for w in arr2:
        if w > limit:
            result += power
        else:
            result += w

    return result


