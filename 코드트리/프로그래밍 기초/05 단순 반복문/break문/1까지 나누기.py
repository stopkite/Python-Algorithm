n = int(input())
a = 1
cnt = 0

while n > 1:
    n //= a
    a += 1
    cnt += 1

print(cnt)