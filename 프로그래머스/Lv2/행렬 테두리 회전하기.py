def solution(rows, columns, queries):
    answer = []

    # 배열 만들기
    arr = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            arr[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        # 맨 위의 맨 왼쪽 값을 기록
        start_point = arr[x1][y1]
        min_value = start_point
        # 왼쪽
        for k in range(x1, x2):
            arr[k][y1] = arr[k + 1][y1]
            min_value = min(min_value, arr[k + 1][y1])
        # 아래
        for k in range(y1, y2):
            arr[x2][k] = arr[x2][k + 1]
            min_value = min(min_value, arr[x2][k + 1])
        # 오른쪽
        for k in range(x2, x1, -1):
            arr[k][y2] = arr[k - 1][y2]
            min_value = min(min_value, arr[k - 1][y2])
        # 위
        for k in range(y2, y1 + 1, -1):
            arr[x1][k] = arr[x1][k - 1]
            min_value = min(min_value, arr[x1][k - 1])

        arr[x1][y1+1] = start_point

        # 테두리 최솟값 구하기
        answer.append(min_value)

    return answer
