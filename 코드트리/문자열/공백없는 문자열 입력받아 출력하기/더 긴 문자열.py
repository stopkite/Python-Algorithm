word1, word2 = input().split()

if len(word1) > len(word2):
    print(word1, len(word1))
elif len(word2) > len(word1):
    print(word2, len(word2))
else:
    print("same")