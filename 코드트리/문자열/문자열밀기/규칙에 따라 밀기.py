word = input()
order = list(input())

for o in order:
    if o == 'L':
        word = word[1:] + word[0]
    else:
        word = word[-1] + word[:-1]

print(word)