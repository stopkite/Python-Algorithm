from collections import deque


def solution(priorities, location):
    cnt = 0
    p = deque(priorities)
    while p:
        max_value = max(p)
        front = p.popleft()
        location -= 1

        if max_value == front:
            cnt += 1
            if location < 0:
                return cnt
        else:
            p.append(front)
            if location < 0:
                location = len(p) - 1
