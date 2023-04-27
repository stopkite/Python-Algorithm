a = int(input())
t = int(input())
type = int(input())

arr = []
b = 1
d = 1
turn = 0

while True:
    prev_b = b
    turn += 1

    for _ in range(2):
        arr.append((b, 0))
        b += 1
        arr.append((d, 1))
        d += 1

    for _ in range(turn + 1):
        arr.append((b, 0))
        b += 1

        arr.append((d, 1))
        d += 1

    if t <= b and t > prev_b:
        print(arr.index((t, type)) % a)
        break