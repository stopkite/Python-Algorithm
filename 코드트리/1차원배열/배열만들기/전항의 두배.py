arr = [0 for _ in range(11)]

arr[1], arr[2] = map(int ,input().split())

for i in range(3, 11):
    arr[i] = arr[i - 1] + 2 * arr[i-2]

for elem in arr[1:11]:
    print(elem, end=" ")