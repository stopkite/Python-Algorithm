while True:
    arr = input().split()
    w, h, c = int(arr[0]), int(arr[1]), arr[2]

    print(w * h)

    if c == 'C':
        break
