while True:
    stack = []
    s = input()
    if s == ".":
        break

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == '[':
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

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
