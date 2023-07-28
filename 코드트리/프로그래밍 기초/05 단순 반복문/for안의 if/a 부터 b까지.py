arr = input().split()
a, b = int(arr[0]), int(arr[1])

while a <= b:
    print(a, end=" ")

    if a % 2 == 0:
        a += 3
    else:
        a = (2 * a)
