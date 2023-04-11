n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

flag = False
count = 0

for i in range(n1):
    if arr1[i] == arr2[count]:
        count += 1
    else:
        count = 0

    if count == n2:
        flag = True
        break

if flag == True:
    print("Yes")
else:
    print("No")