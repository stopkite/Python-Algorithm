from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    q = deque(list(map(int, input().split())))
    order = deque(list(range(n)))

    while q:
        if q[0] == max(q):
            q.popleft()



