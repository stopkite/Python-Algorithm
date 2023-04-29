from itertools import combinations

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

com = []
for i in range(1, n + 1):
    com.append(combinations(arr, i))

ans = 1000000000
for line in com:
    for each in line:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]

        ans = min(ans, abs(sour - bitter))

print(ans)
