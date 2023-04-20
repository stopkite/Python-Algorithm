n = int(input())
word_list = [input() for _ in range(n)]

cnt_a = 0
cnt_word = 0
for word in word_list:
    if word[0] == 'a':
        cnt_a += 1
    cnt_word += len(word)

print(cnt_word, cnt_a)