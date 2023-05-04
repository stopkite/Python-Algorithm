word = list(input())

while len(word) > 1:
    n = int(input())

    if n > len(word) - 1:
        word.pop()
    else:
        word.pop(n)

    print(''.join(word))