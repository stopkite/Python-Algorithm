from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    arr = sys.stdin.readline().split()
    order = arr[0]

    if order == "push_front":
        value = int(arr[1])
        q.appendleft(value)

    elif order == "push_back":
        value = int(arr[1])
        q.append(value)

    elif order == "pop_front":
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)

    elif order == "pop_back":
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)

    elif order == "size":
        print(len(q))

    elif order == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif order == "front":
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)

    else:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
