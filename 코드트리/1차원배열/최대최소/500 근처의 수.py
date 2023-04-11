arr = list(map(int, input().split()))

min_arr = []
max_arr = []

for elem in arr:
    if elem > 500:
        min_arr.append(elem)

    if elem < 500:
        max_arr.append(elem)

print(max(max_arr), min(min_arr))

