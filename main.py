arr = [[-1] * 15 for i in range(5)]

for i in range(5):
    s = list(input())

    for j in range(len(s)):
        arr[i][j] = s[j]

for i in range(15):
    for j in range(5):
        if arr[j][i] != -1:
            print(arr[j][i], end="")
