"""while True:
    string = input()

    if string == "END":
        break

    for elem in string[::-1]:
        print(elem, end="")

    print() """

while True:
    password = input()

    if password == 'END':
        break
    else:
        print(password[::-1])