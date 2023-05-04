word = input()

cnt_ee, cnt_eb = 0, 0
for i in range(len(word)-1):
    if word[i] == 'e':
        if word[i + 1] == 'e':
            cnt_ee += 1
        elif word[i + 1] == 'b':
            cnt_eb += 1

print(cnt_ee, cnt_eb)