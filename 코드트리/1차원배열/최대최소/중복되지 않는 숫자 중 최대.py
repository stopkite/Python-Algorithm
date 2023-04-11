n = int(input())
arr = list(map(int, input().split()))

count_arr = []

for elem in arr:
    if arr.count(elem) <= 1:
        count_arr.append(elem)

if len(count_arr) == 0:
    print("-1")
else:
    print(max(count_arr))