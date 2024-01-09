from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    target = (s1 + s2) // 2

    while q2:
        if s1 > target:
            value = q1.popleft()
            s1 -= value
        elif s1 < target:
            value = q2.popleft()
            q1.append(value)
            s1 += value
        else:
            return answer
        answer += 1
    return -1