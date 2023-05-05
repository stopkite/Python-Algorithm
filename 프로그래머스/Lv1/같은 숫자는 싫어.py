def solution(arr):
    answer = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])

    if len(answer) == 0:
        answer.append(arr[0])
    else:
        if answer[-1] != arr[-1]:
            answer.append(arr[-1])

    return answer