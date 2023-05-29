n = int(input())
arr = []
reverse_arr = []
for _ in range(n):
    s = input()
    arr.append(s)
    reverse_arr.append(s[::-1])

l = 0
answer = ''

for i in arr:
    if i in reverse_arr:
        l = len(i)
        answer = i[l//2]
        break

print(l, answer)
