def solution(new_id):
    # 1단계
    answer = new_id.lower()

    # 2단계
    result = ''
    for s in answer:
        if s.islower() or s.isnumeric():  # 알파벳, 소문자, 숫자
            result += s
        if s == "-" or s == "_" or s == ".":  # 빼기, 밑줄, 마침표 제외
            result += s
    answer = result

    # 3단계
    # 연속 마침표 제외
    while '..' in answer:
        answer = answer.replace("..", ".")

    # 4단계
    if answer[0] == ".":  # 처음에 마침표(.)가 들어가있을 때
        answer = answer[1:]
    if len(answer) != 0:
        if answer[-1] == ".": # 끝에 마침표(.)가 들어갔을 때
            answer = answer[:-1]

    # 5단계
    if not answer:  # 빈 문자열에 a 대입
        answer = "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]  # 첫 15개 문자를 제외한 나머지 문자열 모두 제거
        if answer[-1] == ".":  # 끝자리 마침표(.) 제거
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while len(answer) != 3:  # 마지막 문자를 길이가 3이 될때까지 반복 추가
            answer += answer[-1]

    return answer