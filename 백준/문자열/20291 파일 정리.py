n = int(input())

fileList = dict()
for _ in range(n):
    end = input().split('.')[1]
    if end in fileList:
        fileList[end] += 1
    else:
        fileList[end] = 1

sort_fileList = sorted(fileList.items())

for k, v in sort_fileList:
    print(k, v)
