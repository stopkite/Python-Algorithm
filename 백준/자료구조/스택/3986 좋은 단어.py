t = int(input())
answer = 0
for _ in range(t):
    temp = []
    word = input()

    if len(word) % 2 != 0:
        continue

    for i in range(len(word)):
        if not temp:
            temp.append(word[i])
        else:
            if word[i] == temp[-1]:
                temp.pop()
            else:
                temp.append(word[i])

    if not temp:
        answer += 1

print(answer)

