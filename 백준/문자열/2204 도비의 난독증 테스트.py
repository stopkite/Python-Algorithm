while True:
    n = int(input())
    if n == 0:
        break
    temp = []
    for _ in range(n):
        word = input()
        temp.append(word)

    print(sorted(temp, key=lambda x: x.lower())[0])
