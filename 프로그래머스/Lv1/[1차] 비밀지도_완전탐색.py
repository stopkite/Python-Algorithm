def solution(n, arr1, arr2):
    answer = []

    bin_arr1 = []
    for num in arr1:
        if len(bin(num)[2:]) < n:
            bin_arr1.append('0' * (n - len(bin(num)[2:])) + bin(num)[2:])
        else:
            bin_arr1.append(bin(num)[2:])

    bin_arr2 = []
    for num in arr2:
        if len(bin(num)[2:]) < n:
            bin_arr2.append('0' * (n - len(bin(num)[2:])) + bin(num)[2:])
        else:
            bin_arr2.append(bin(num)[2:])

    answer = []
    for i in range(n):
        res = ''
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                res += '#'
            else:
                res += ' '
        answer.append(res)

    return answer
