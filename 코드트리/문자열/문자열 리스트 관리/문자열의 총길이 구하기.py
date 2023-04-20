word_list = input().split()
cnt = 0
for word in word_list:
    cnt += len(word)
print(cnt)