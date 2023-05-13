from collections import deque


def solution(s):
    answer = True
    s = list(s)
    stack = deque([])

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.popleft()

    if stack:
        answer = False

    return answer