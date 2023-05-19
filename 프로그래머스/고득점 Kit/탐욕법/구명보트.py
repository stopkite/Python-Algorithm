from collections import deque

def solution(people, limit):
    cnt = 0
    people = deque(sorted(people))

    while people:
        if len(people) == 1:
            cnt += 1
            break

        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            cnt += 1
        else:
            people.pop()
            cnt += 1

    return cnt
