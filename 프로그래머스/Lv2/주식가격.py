def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1

            if prices[i] > prices[j]:
                answer.append(cnt)
                break

            if j == len(prices) - 1:
                answer.append(cnt)
                break

    answer.append(0)

    return answer