satisfied = True
arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

for i in range(a, b + 1):
    if i % c == 0:
        satisfied = False

print("YES" if satisfied == True else "NO")