files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
head = {}
number = {}
tail = {}
for idx, file in enumerate(files):
    h, n, t = '', '', ''
    last_numeric_idx = 0
    for i in range(len(file)):
        if not file[i].isnumeric():  # head
            h += file[i]

            if i > last_numeric_idx:  # tail
                t += file[i]

        else:  # number
            n += file[i]
            last_numeric_idx = i
    print(idx)

print(head)
print(number)
print(tail)