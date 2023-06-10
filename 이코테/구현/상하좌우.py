n = int(input())
move = list(map(str, input().split()))

i, j = 0, 0

for m in move:
    if m == 'L':
        if j - 1 < 0:
            continue
        j = j - 1
    elif m == 'R':
        if j + 1 >= n:
            continue
        j = j + 1
    elif m == 'U':
        if i - 1 < 0:
            continue
        i = i - 1
    else:
        if i + 1 >= n:
            continue
        i = i + 1

print(i + 1, j + 1)
