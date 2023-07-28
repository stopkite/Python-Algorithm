n = int(input())
cnt = 'A'

for i in range(n):
    for j in range(i + 1):
        print(cnt, end="")
        cnt = chr(ord(cnt) + 1)
        if ord(cnt) > ord('Z'):
            cnt = 'A'
    print()