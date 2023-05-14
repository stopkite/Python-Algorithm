import sys

n = int(sys.stdin.readline())
circles = []

for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x - r, i))
    circles.append((x + r, i))

circles.sort()

stack = []
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)

if stack:
    print('NO')
else:
    print('YES')