n = int(input())
last_name = []
for _ in range(n):
    s = input()
    last_name.append(s[0])

res = []
for ln in last_name:
    if last_name.count(ln) >= 5:
        res.append(ln)

if not res:
    print("PREDAJA")
else:
    result = ''.join(sorted(list(set(res))))
    print(result)




