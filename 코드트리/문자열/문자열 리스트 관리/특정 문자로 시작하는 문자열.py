n = int(input())
word_list = [input() for _ in range(n)]
a = input()

cnt = 0
len_cnt = 0
for w in word_list:
    if w[0] == a:
        cnt += 1
        len_cnt += len(w)

print(f"{cnt} {len_cnt/cnt:.2f}")