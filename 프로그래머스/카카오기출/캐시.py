from collections import deque


def solution(cacheSize, cities):
    answer = 0
    caches = deque([])

    for city in cities:
        city = city.upper()
        if cacheSize != 0:
            if city not in caches:
                if len(caches) == cacheSize:
                    caches.pop()
                answer += 5
            else:
                caches.remove(city)
                answer += 1
        else:
            answer += 5

        caches.appendleft(city)
    return answer


solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
             "Rome"])
solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
             "Rome"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(0, ["Jeju", "Jeju", "Jeju", "Jeju", "Jeju"])
