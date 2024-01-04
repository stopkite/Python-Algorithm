from itertools import combinations


def solution(relation):
    column, row = len(relation[0]), len(relation)

    def is_minimal_key(combination, candidate_keys):
        for key in candidate_keys:
            if key.issubset(combination):
                return False
        return True

    all_keys = []
    for r in range(1, column + 1):
        for combination in combinations(range(column), r):
            all_keys.append(set(combination))

    candidate_keys = []
    for key in all_keys:
        row_set = set()
        for r in range(row):
            row_str = ""
            for elem in key:
                row_str += relation[r][elem]
            row_set.add(row_str)

        # 유일성, 최소성 체크
        if len(row_set) == row and is_minimal_key(key, candidate_keys):
            candidate_keys.append(key)

    return len(candidate_keys)


result = solution([
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]
])

print(result)
