word = input()

ans = ''

cur_char = word[0]
cnt = 1
for target_char in word[1:]:
    if target_char == cur_char:
        cnt += 1
    else:
        ans += cur_char
        ans += str(cnt)

        cur_char = target_char
        cnt = 1

ans += cur_char
ans += str(cnt)

print(len(ans))
print(ans)