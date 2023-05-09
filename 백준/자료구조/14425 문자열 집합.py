n, m = map(int, input().split())
s = []
for _ in range(n):
    word = input()
    s.append(word)

cnt = 0
for _ in range(m):
    word = input()
    if word in s:
        cnt += 1

print(cnt)