from itertools import combinations

n, m = map(int, input().split())
ice = [[False] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    ice[a - 1][b - 1] = True
    ice[b - 1][a - 1] = True

result = 0

for i in combinations(range(n), 3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    result += 1

print(result)
