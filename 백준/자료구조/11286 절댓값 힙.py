import sys
import heapq

n = int(input())
q = []

for _ in range(n):
    a = int(sys.stdin.readline().strip())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
