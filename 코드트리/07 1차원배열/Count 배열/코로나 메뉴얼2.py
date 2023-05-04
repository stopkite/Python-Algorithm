cnt_arr = [0] * 4

for _ in range(3):
    a, b = input().split()
    b = int(b)

    if a == 'Y':
        if b >= 37:
            cnt_arr[0] += 1 # A
        else:
            cnt_arr[2] += 1 # C
    else:
        if b >= 37:
            cnt_arr[1] += 1 # B
        else:
            cnt_arr[3] += 1 # D

for elem in cnt_arr:
    print(elem, end=" ")

if cnt_arr[0] >= 2:
    print("E")