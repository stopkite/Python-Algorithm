from collections import deque


def solution(info, edges):
    n = len(info)

    visited = [False] * n

    graph = [[] for _ in range(n)]
    for parent, child in edges:
        graph[parent].append(child)

    cnts = [(0, 0) for _ in range(n)]  # sheep, wolf

    q = deque([0])
    cnts[0] = (1, 0)
    while q:
        cur_v = q.popleft()
        visited[cur_v] = True

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)

                cur_sheep, cur_wolf = cnts[cur_v]
                if info[next_v] == 0:
                    cur_sheep += 1
                else:
                    cur_wolf += 1

                cnts[next_v] = (cur_sheep, cur_wolf)

    filtered_cnts = [t for t in cnts if t[0] > t[1]]
    answer = max(filtered_cnts)[0]
    return answer


print(solution(	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))