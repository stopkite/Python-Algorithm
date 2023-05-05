def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = str(bin(i | j)[2:]).rjust(n, '0')
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)

    return answer