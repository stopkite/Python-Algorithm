import heapq

n = int(input())
q = []
for _ in range(n):
    temp = list(map(int, input().split()))
    if not q:
        for num in temp:
            heapq.heappush(q, num)
    else:
        for num in temp:
            if num > q[0]:
                heapq.heappush(q, num)
                heapq.heappop(q)
print(q[0])
