a, b, c, m = map(int, input().split())

tired = 0
work = 0

for i in range(24):
    if tired + a <= m:
        tired += a
        work += b
    else:
        if tired - c < 0:
            tired = 0
        else:
            tired -= c

print(work)
