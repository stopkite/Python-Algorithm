n = int(input())

for i in range(n):
    for j in range(n):
        print(f"({n - i},{n - j})", end=" ")
    print()