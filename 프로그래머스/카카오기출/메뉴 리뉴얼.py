from itertools import combinations


def solution(orders, course):
    # 코스요리 후보 조합 추가
    course_combinations = {}
    for course_length in course:
        for order in orders:
            for comb in combinations(sorted(order), course_length):
                temp = ''.join(comb)  # AB, AC, AD ...
                if temp not in course_combinations:
                    course_combinations[temp] = 1
                else:
                    course_combinations[temp] += 1

    # 2명 이상이 주문한 조합 필터링
    course_combinations = {k: v for k, v in course_combinations.items() if v >= 2}

    answer = []
    # 코스 요리 중에 가장 많은 사람이 원했던 코스 고르기
    for course_length in course:
        max_count = 2
        for course_key, count in course_combinations.items():  # 최댓값 찾기
            if len(course_key) == course_length:
                max_count = max(max_count, count)

        for course_key, count in course_combinations.items():  # 최댓값을 가진 메뉴들 넣기
            if max_count == count and len(course_key) == course_length:
                answer.append(course_key)

    return sorted(list(set(answer)))


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print("————")
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print("————")
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
print("————")
