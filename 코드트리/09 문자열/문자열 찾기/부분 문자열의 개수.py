a = input()
b = input()

cnt = 0
for i in range(len(a)-1):
    if a[i] == b[0] and a[i + 1] == b[1]:
        cnt += 1

print(cnt)