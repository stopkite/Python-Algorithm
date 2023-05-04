arr = input().split()
mid, fin = int(arr[0]), int(arr[1])

if mid >= 90:
    if fin >= 95:
        print(100000)
    elif fin >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)