n = int(input())
arr = list(map(int, input().split()))

print(min(arr), arr.count(min(arr)))