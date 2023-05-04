n = int(input())

if n >= 1 and n <= 12:
    if n == 2:
        print(28)
    elif n == 4 or n == 6 or n == 9 or n == 11:
        print(30)
    else:
        print(31)