cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for c in cro:
    word = word.replace(c, '0')

print(len(word))