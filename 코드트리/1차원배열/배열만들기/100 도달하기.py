n = int(input())

arr = [1, n]

for i in range(0, 100):
    sum_val = arr[-1] + arr[-2]
    arr.append(sum_val)

    if sum_val > 100:
        break


for elem in arr:
    print(elem, end=" ")