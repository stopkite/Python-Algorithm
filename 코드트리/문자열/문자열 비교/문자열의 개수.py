arr = []
cnt = 0
while True:
    word = input()

    if word == '0':
        break
    if (cnt + 1) % 2 == 1:
        arr.append(word)

    cnt += 1

print(cnt)

for elem in arr:
    print(elem)
