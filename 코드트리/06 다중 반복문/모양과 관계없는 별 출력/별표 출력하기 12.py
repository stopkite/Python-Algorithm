n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            if i == 0:
                print("* ", end="")
            else:
                print("  ", end="")
        else:
            if i <= j:
                print("* ", end="")
            else:
                print("  ", end="")
    print()