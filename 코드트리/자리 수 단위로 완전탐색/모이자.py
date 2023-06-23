import sys

n = int(input())
d = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(len(d)):
    distance = 0
    for j in range(len(d)):
        distance += abs((j - i)) * d[j]

    min_val = min(min_val, distance)

print(min_val)
