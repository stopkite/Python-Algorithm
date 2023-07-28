n = int(input())

for i in range(n):
    if i == 0:
        for _ in range(n):
            print("*", end=" ")
        print()
    else:
        for j in range(n):
            if j == (n - 1):
                print("*", end="")
            elif j <= i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()