from itertools import permutations


def solution(k, dungeons):
    clears = []
    d_permutations = list(permutations(dungeons, len(dungeons)))

    for case in d_permutations:
        clear = 0
        hp = k

        for d in case:
            if hp >= d[0]:
                hp -= d[1]
                clear += 1

        clears.append(clear)

    return max(clears)