arr = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()
    flag = False

    if word == 'end':
        break

    for a in word:  # 모음이 들어 있는지 검사
        if a in arr:
            flag = True

    for i in range(len(word) - 2):  # 연속된 3 단어 검사
        if (word[i] in arr) and (word[i + 1] in arr) and (word[i + 2] in arr):
            flag = False

        if (word[i] not in arr) and (word[i + 1] not in arr) and (word[i + 2] not in arr):
            flag = False

    for i in range(len(word) - 1):  # 연속된 두 단어 검사
        if word[i] == word[i + 1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            flag = False

    if flag:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
