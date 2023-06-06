n = int(input())
cnt = 0
for _ in range(n):
    s = input()

    cur = ''
    flag = True
    temp = []
    for i in range(len(s)):
        if s[i] != cur:
            if s[i] in temp:
                flag = False
                break
            else:
                temp.append(s[i])
        cur = s[i]

    if flag:
        cnt += 1

print(cnt)
