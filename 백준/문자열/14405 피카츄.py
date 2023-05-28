word = input()

word = word.replace("pi","0")
word = word.replace("ka","0")
word = word.replace("chu","0")

flag = True
for w in word:
    if w != '0':
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")