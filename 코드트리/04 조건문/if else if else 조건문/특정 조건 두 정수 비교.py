arr = input().split()
a1, a2 = int(arr[0]), int(arr[1])

if a1 < a2:
    print(1, end=" ")
else:
    print(0, end=" ")

if a1 == a2:
    print(1)
else:
    print(0)