n = int(input())
arr = list(map(int, input().split()))
line = [0 for _ in range(n)]

for p in range(1, n + 1):
    temp = arr[p - 1]
    cnt = 0
    for i in range(n):
        if cnt == temp and line[i] == 0:
            line[i] = p
            break
        elif line[i] == 0:
            cnt += 1

for elem in line:
    print(elem, end=" ")
