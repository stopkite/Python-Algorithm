n = int(input())

arr = {}
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a not in arr:
        arr[a] = b
    else:
        if arr[a] != b:
            cnt += 1
            arr[a] = b
print(cnt)
