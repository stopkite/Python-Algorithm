word = input()

for i in range(len(word)):
    if word[i].isalpha():
        print(word[i].upper(),end="")