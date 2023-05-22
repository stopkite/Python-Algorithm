def solution(dartResult):
    turn = 0
    dartResult = dartResult.replace("10", "X")
    scores = []
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric() or dartResult[i] == 'X':  # 점수
            if dartResult[i] == "X":
                scores.append(10)
            else:
                scores.append(int(dartResult[i]))
            turn += 1
        elif dartResult[i].isalpha():  # 보너스
            if dartResult[i] == 'S':
                scores[-1] = scores[-1] ** 1
            elif dartResult[i] == 'D':
                scores[-1] = scores[-1] ** 2
            elif dartResult[i] == 'T':
                scores[-1] = scores[-1] ** 3
        else:  # 옵션
            if dartResult[i] == '*':
                if turn == 1:  # 1번째 턴
                    scores[0] *= 2
                elif turn == 2:  # 2번째 턴
                    scores[0] *= 2
                    scores[1] *= 2
                else:  # 3번째 턴
                    scores[1] *= 2
                    scores[2] *= 2
            elif dartResult[i] == '#':
                idx = turn - 1
                scores[idx] *= -1

    return sum(scores)
