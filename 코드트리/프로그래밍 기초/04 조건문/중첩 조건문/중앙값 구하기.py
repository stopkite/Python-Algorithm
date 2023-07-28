arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a > b:
    if c > a:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
else:
    if c > b:
        print(b)
    elif a > c:
        print(b)
    else:
        print(c)
