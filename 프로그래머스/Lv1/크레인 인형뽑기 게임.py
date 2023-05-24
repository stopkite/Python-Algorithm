def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        j = move - 1
        for i in range(len(board)):
            if board[i][j] > 0:
                basket.append(board[i][j])
                board[i][j] = 0
                break

        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2

    return answer
