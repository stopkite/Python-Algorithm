word = input()
answer = ''
for w in word:
    if w.isupper():
        answer += w.lower()
    else:
        answer += w.upper()
print(answer)