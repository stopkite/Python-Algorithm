from collections import deque


def solution(n, words):
    speaker = 1
    turn = 1
    stack = []

    words = deque(words)
    while words:
        speaker += 1
        if speaker > n:
            speaker %= n
            turn += 1

        current_word = words.popleft()
        stack.append(current_word)

        if not words:  # 스택이 비어 있다면
            return [0, 0]

        if current_word[-1] != words[0][0]:  # 처음과 끝이 다르다면
            break

        if words[0] in stack:  # 이미 말한 단어라면
            break

    answer = [speaker, turn]

    return answer
