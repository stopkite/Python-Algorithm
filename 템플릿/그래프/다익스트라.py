import heapq

v, e = map(int, input().split())  # v: 정점, e: 간선

start = int(input())

graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, dist = map(int, input().split())  # dist: 거리
    graph[a].append((dist, b))


def dijsktra(start):
    pq = []
    costs = {}
    heapq.heappush(pq, (0, start))  # 처음 시작점은 거리가 0
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    for v in range(1, len(graph)):
        if v not in costs:
            print("INF")
        else:
            print(costs[v])


dijsktra(start)
