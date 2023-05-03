from collections import deque

n = int(input())
numbers = list(map(int, input().split()))

balloons = deque([])
for i in range(n):
    balloons.append((i + 1, numbers[i]))

while balloons:
    b = balloons[0][0]  # 풍선 번호
    num = balloons[0][1]  # 종이 번호

    print(b, end=" ")  # 풍선번호 출력
    balloons.popleft()  # 뽑은 풍선 제거

    if num > 0:
        balloons.rotate(-(num - 1))
    else:
        balloons.rotate(-num)
