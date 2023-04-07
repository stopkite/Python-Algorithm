arr = list(map(int, input().split()))

for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 0:
        print(elem // 2, end=" ")
    else:
        print(elem + 3, end=" ")