while True:
    try:
        s, t = input().split()

        value = 0
        flag = False

        for i in range(len(t)):
            if t[i] == s[value]:
                value += 1
                if value == len(s):
                    flag = True
                    break

        if flag == True:
            print('Yes')
        else:
            print('No')

    except:
        break
