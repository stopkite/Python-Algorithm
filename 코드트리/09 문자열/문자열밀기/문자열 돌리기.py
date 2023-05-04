word = input()

l = len(word)
print(word)
for _ in range(l):
    word = word[-1] + word[:-1]
    print(word)