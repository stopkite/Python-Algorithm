n = int(input())

cnt = 0

for _ in range(n):
    score = list(map(int, input().split()))
    avg_val = sum(score) / 4

    if avg_val >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)
