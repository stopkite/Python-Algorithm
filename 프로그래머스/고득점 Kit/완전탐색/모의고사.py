def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt1 = 0
    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            cnt1 += 1

    cnt2 = 0
    for i in range(len(answers)):
        if answers[i] == s2[i % 8]:
            cnt2 += 1

    cnt3 = 0
    for i in range(len(answers)):
        if answers[i] == s3[i % 10]:
            cnt3 += 1

    counts = [cnt1, cnt2, cnt3]
    max_value = max(counts)
    answer = []
    for i in range(0, 3):
        if max_value == counts[i]:
            answer.append(i + 1)
    return answer