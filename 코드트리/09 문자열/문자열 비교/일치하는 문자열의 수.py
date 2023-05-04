n, a = input().split()

cnt = 0
for _ in range(int(n)):
    s = input()
    if s == a:
        cnt += 1

print(cnt)