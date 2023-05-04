for i in range(1, 20):
    for j in range(1, 20):
        if j % 2 == 1:
            print(f"{i} * {j} = {i * j}", end="")
        elif j % 2 == 0:
            print(f" / {i} * {j} = {i * j}", end="\n")

        if j == 19:
            print()