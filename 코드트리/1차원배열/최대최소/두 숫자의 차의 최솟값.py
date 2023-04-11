n = int(input())
arr = list(map(int, input().split()))

arr_diff = []

for i in range(n):
    for j in range(i+1,n):
        arr_diff.append(abs(arr[j]-arr[i]))

print(min(arr_diff))