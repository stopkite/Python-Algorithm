n = int(input())
a = list(input())

a_len = len(a)
for i in range(n - 1):
    s = list(input())
    for j in range(a_len):
        if a[j] != s[j]:
            a[j] = '?'

print(''.join(a))
