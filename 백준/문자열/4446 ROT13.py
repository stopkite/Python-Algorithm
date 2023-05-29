def rot_13(s):
    a = ['a', 'i', 'y', 'e', 'o', 'u']
    b = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

    dic = {}

    for i in a:
        idx = a.index(i)
        new_idx = idx + 3
        if new_idx >= len(a):
            new_idx -= len(a)
        dic[i] = a[new_idx]

    for i in b:
        idx = b.index(i)
        new_idx = idx + 10
        if new_idx >= len(b):
            new_idx -= len(b)
        dic[i] = b[new_idx]

    result = ''
    for i in s:
        if i.isupper():
            temp = dic[i.lower()]
            result += temp.upper()
        elif i.islower():
            result += dic[i]
        else:
            result += i

    print(result)


while True:
    try:
        s = input()
        rot_13(s)
    except:
        break
