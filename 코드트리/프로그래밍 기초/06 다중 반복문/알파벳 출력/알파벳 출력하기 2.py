n = int(input())
cnt = 'A'

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(cnt, end=" ")
            cnt = chr(ord(cnt) + 1)
            if ord(cnt) > ord('Z'):
                cnt = 'A'
    print()
