n = int(input())

rope_arr = []
for _ in range(n):
    rope_arr.append(int(input()))

rope_arr.sort(reverse=True)
result = []
for i in range(len(rope_arr)):
    result.append(rope_arr[i] * (i + 1))

print(max(result))
