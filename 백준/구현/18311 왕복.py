n, k = map(int, input().split())
distance = list(map(int, input().split()))

answer = 0
for i in range(len(distance)):
    k -= distance[i]
    if k < 0:
        answer = i + 1
        break

if k >= 0:
    for i in range(len(distance) - 1, -1, -1):
        k -= distance[i]
        if k < 0:
            answer = i + 1
            break
print(answer)
