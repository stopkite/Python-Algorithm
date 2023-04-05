n = int(input())
arr = list(map(int,input().split()))

arr_2d = []
for elem in arr:
    if elem % 2 == 0:
        arr_2d.append(elem)

for elem in arr_2d[::-1]:
    print(elem, end=" ")