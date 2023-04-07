n = int(input())
arr = list(map(int, input().split()))

for elem in arr:
    if elem % 2 == 0:
        print(elem, end=" ")