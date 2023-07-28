a, b = map(int, input().split())
cnt_arr = [0] * (b + 1)
ans = 0

while a > 1:
    cnt_arr[a % b] += 1
    a //= b

for elem in cnt_arr:
    ans += elem ** 2

print(ans)