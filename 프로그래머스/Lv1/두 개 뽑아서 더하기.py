from itertools import permutations


def solution(numbers):
    answer = []
    for i, j in permutations(numbers, 2):
        answer.append(i + j)

    answer = list(set(answer))
    answer.sort()

    return answer