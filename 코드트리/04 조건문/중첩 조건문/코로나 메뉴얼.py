arr = input().split()
a1, a2 = arr[0], int(arr[1])

arr = input().split()
b1, b2 = arr[0], int(arr[1])

arr = input().split()
c1, c2 = arr[0], int(arr[1])

cnt = 0

if a1 == 'Y':
    if a2 >= 37:
        cnt += 1

if b1 == 'Y':
    if b2 >= 37:
        cnt += 1

if c1 == 'Y':
    if c2 >= 37:
        cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")