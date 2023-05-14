n = int(input())
arr = [i for i in range(1, n + 1)]

while len(arr) != 1:
    temp = []
    for i in range(0, len(arr), 2):
        temp.append(arr[i])

    for elem in temp:
        arr.remove(elem)

print(arr[0])
