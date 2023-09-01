n = int(input())
numbers = [int(input()) for _ in range(n)]

positive_nums = []
negative_nums = []
is_zero_exist = False
for num in numbers:
    if num == 0:
        is_zero_exist = True
    elif num > 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)

positive_nums.sort()  # 1 3 5
negative_nums.sort()  # -5 -3 -1

# 음수 o, 0 존재 -> 가장 큰 음수랑 곱하기
# 음수 o, 0 부재 -> 음수까리 곱하기
# 음수 x, 0 존재 -> 더하기
# 음수 x, 0 부재 -> 양수 곱하기
total_num = 0
if negative_nums:
    if is_zero_exist:
        negative_nums.pop()  # 0 이랑 곱하기 때문에 없애주기
        while len(negative_nums) != 1:  # 하나 남을 때까지 뽑기
            n1 = negative_nums.pop()
            n2 = negative_nums.pop()
            total_num += (n1 * n2)
    else:
        while len(negative_nums) != 1:
            n1 = negative_nums.pop()
            n2 = negative_nums.pop()
            total_num += (n1 * n2)
else:
    if is_zero_exist:
        while len(negative_nums)



