from itertools import combinations

n, m = map(int, input().split())
likes = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for a, b, c in combinations(range(m), 3):
    temp_sum = 0
    for i in range(n):
        temp_sum += max(likes[i][a], likes[i][b], likes[i][c])

    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)
