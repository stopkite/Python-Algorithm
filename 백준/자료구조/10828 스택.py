from sys import stdin


def solution(n: int):
    stack = []
    for _ in range(n):
        arr = stdin.readline().split()
        order = arr[0]

        if order == "push":
            number = int(arr[1])
            stack.append(number)

        elif order == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop(-1))

        elif order == "size":
            print(len(stack))

        elif order == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)

        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])


solution(int(stdin.readline()))
