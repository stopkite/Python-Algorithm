s = list(input())
k = input()

arr = []
for a in s:
    if (ord(a) >= 65 and ord(a) < 91) or (ord(a) >= 97 and ord(a) < 123):
        arr.append(a)

new_s = ''.join(arr)

if k in new_s:
    print(1)
else:
    print(0)
