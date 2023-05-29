from collections import deque


def solution(s):
    answer = 0
    s = deque(s)

    for _ in range(len(s)):
        s.rotate(-1)
        if check_correct_word(s):
            answer += 1
    return answer


def check_correct_word(s):
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')':
            stack.append(i)
            if len(stack) >= 2 and stack[-2] == '(':
                stack.pop()
                stack.pop()
        elif i == ']':
            stack.append(i)
            if len(stack) >= 2 and stack[-2] == '[':
                stack.pop()
                stack.pop()
        elif i == '}':
            stack.append(i)
            if len(stack) >= 2 and stack[-2] == '{':
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False
