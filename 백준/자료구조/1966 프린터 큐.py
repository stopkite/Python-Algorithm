from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    count = 0
    while q:
        max_value = max(q)
        front = q.popleft()
        m -= 1

        if max_value == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            q.append(front)
            if m < 0:
                m = len(q) - 1
