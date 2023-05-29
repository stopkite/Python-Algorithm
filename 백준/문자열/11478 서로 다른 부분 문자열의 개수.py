s = input()
arr = []
for i in range(len(s)):
    for j in range(i, len(s)):
        arr.append(s[i:j + 1])

print(len(set(arr)))
