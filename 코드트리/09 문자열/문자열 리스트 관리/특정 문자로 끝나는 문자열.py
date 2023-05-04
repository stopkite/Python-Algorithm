word_list = []
for _ in range(10):
    word_list.append(input())

a = input()
flag = False

for word in word_list:
    if word[-1] == a:
        print(word)
        flag = True

if flag == False:
    print("None")