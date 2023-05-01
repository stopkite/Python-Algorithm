from collections import deque
import sys


def solution(n: int):
    q = deque()
    for _ in range(n):
        arr = sys.stdin.readline().split()
        order = arr[0]

        if order == "push":
            number = int(arr[1])
            q.append(number)

        elif order == "pop":
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())

        elif order == "size":
            print(len(q))

        elif order == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)

        elif order == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])

        else:
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])


solution(int(sys.stdin.readline()))
