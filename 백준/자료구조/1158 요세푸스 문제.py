from collections import deque

n, k = map(int, input().split())
arr = []
q = deque()

for i in range(1, n + 1):
    q.append(i)

for i in range(len(q)):
    q.rotate(-(k-1))
    print(q)
    arr.append(str(q.popleft()))

print("<", end="")
print(', '.join(arr), end="")
print(">", end="")
