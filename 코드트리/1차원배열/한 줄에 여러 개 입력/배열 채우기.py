arr = list(map(int,input().split()))

arr.pop()

for elem in arr[::-1]:
    print(elem, end=" ")