word = list(input())
first = word[0]
sec = word[1]

for i in range(len(word)):
    if word[i] == first:
        word[i] = sec
    elif word[i] == sec:
        word[i] = first

print("".join(word))