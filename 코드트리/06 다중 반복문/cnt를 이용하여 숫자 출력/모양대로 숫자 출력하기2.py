n = int(input())
cnt = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(cnt * 2, end=" ")

        cnt += 1

        if cnt == 5:
            cnt = 1
    print()