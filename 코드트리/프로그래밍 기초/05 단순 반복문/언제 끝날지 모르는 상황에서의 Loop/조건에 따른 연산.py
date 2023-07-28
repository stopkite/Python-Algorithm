a = int(input())
n = 0

while True:
    if a >= 1000:
        break

    if a % 2 == 0:
        a = 3 * a + 1
    else:
        a = 2 * a + 2

    n += 1

print(n)
