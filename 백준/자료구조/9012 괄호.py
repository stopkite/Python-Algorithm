def solution(n: int):
    for _ in range(n):
        arr = list(input())
        stack = []

        flag = True
        for elem in arr:
            if elem == '(':
                stack.append('(')
            elif elem == ')':
                if len(stack) != 0:
                    stack.pop()
                else:  # stack 안이 비어 있으면 False
                    flag = False
                    break
            else:  # '(', ')'를 제외한 문자열이 들어오면 continue
                continue

        if len(stack) != 0:  # 스택, 큐 안에 값이 남아 있으면 False
            flag = False

        if flag:  # 괄호 09 문자열 여부 확인
            print("YES")
        else:
            print("NO")


solution(int(input()))
