n = int(input())

for i in range(n):
    for j in range(n-i):
        print('*' * (n - i), end=" ")
    print()