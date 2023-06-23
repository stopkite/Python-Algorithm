def divide(p):
    open = 0
    close = 0

    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        elif p[i] == ')':
            close += 1

        if open == close:
            return p[:i + 1], p[i + 1:]


def is_correct_string(u):
    stack = []
    for s in u:
        if s == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True


def solution(p):
    # step1
    if not p:
        return ""

    # step2
    u, v = divide(p)

    # step3
    if is_correct_string(u):
        return u + solution(v)  # 3-1
    else:
        # step4-1
        answer = '('

        # step4-2
        answer += solution(v)

        # step4-3
        answer += ')'

        # step4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        return answer