n = int(input())
cnt = 9

for i in range(n):
    for j in range(n):
        print(cnt, end="")
        cnt -= 1

        if cnt == 0:
            cnt = 9
    print()