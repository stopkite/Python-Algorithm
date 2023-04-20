words = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()

cnt = 0
for word in words:
    if word[2] == a or word[3] == a:
        print(word)
        cnt += 1

print(cnt)