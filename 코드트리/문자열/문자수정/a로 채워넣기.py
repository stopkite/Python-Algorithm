word = list(input())
word[-2] = "a"
word[1] = "a"

print("".join(word))
