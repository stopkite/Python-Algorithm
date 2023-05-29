import math
s = input()
l = len(s)

if s[0] * l == s:
    print(-1)
elif s[:l//2] == s[math.ceil(l/2):l][::-1]:
    print(l-1)
else:
    print(l)