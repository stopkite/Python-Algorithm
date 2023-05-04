n = int(input())

arr = [n]
cnt5 = 0
for i in range(1, 11):
    arr.append(n * i)

    if (n * i) % 5 == 0:
        cnt5 += 1

    if cnt5 == 2:
        break

for elem in arr[1:]:
    print(elem, end=" ")

