import heapq

INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, dist = map(int, input().split())
    graph[a].append((dist, b))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cur_dist, cur_v = heapq.heappop(q)
        if distance[cur_v] < cur_dist:
            continue
        for dist, next_v in graph[cur_v]:
            next_dist = cur_dist + dist
            if next_dist < distance[next_v]:
                distance[next_v] = next_dist
                heapq.heappush(q, (next_dist, next_v))


dijkstra(start)
