s = input()

for a in s:
    if a.isdigit():
        print(a,end="")
    elif a.isalpha():
        if a.isupper():
            print(a.lower(),end="")
        else:
            print(a,end="")        