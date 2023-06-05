from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    target = (sum(q1) + sum(q2)) / 2

    q1_sum = sum(q1)
    while q1 and q2:
        if q1_sum < target:
            pop_num = q2.popleft()
            q1.append(pop_num)
            q1_sum += pop_num
            answer += 1
        elif q1_sum > target:
            pop_num = q1.popleft()
            q1_sum -= pop_num
            answer += 1
        else:
            return answer
    return -1
