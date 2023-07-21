from collections import deque


def solution(n, k):
    MAX_DISTANCE = 10 ** 5
    distance = [0] * (MAX_DISTANCE + 1)
    moved = [-1, 1, 2]

    start = n
    queue = deque([start])
    while queue:
        x = queue.popleft()

        if x == k:
            break

        for i in range(3):
            if i != 2:
                nx = moved[i] + x
            else:
                nx = moved[i] * x

            if nx < 0 or nx > 100000:
                continue
            if distance[nx] == 0:
                distance[nx] = distance[x] + 1
                queue.append(nx)

    return distance[k]


n, k = map(int, input().split())
print(solution(n, k))
