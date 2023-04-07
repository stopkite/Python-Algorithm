n = int(input())
cnt = n

for _ in range(n):
    word = input()

    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i + 1:]:
                cnt -= 1
                break

print(cnt)

