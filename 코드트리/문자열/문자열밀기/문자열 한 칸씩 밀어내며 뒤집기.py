word, n = input().split()
n = int(n)

for _ in range(n):
    q = int(input())
    if q == 1:
        word = word[1:] + word[0]
    elif q == 2:
        word = word[-1] + word[:-1]
    else:
        word = word[::-1]

    print(word)