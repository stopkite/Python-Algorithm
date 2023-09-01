n = int(input())
numbers = [int(input()) for _ in range(n)]

positive_nums = []
negative_nums = []

result = 0
for num in numbers:
    if num > 1:
        positive_nums.append(num)
    elif num <= 0:
        negative_nums.append(num)
    else:
        result += num

positive_nums.sort(reverse=True)
negative_nums.sort()

# 양수 묶기
for i in range(0, len(positive_nums), 2):
    if i + 1 >= len(positive_nums):
        result += positive_nums[i]
    else:
        result += (positive_nums[i] * positive_nums[i + 1])

# 음수 묶기
for i in range(0, len(negative_nums), 2):
    if i + 1 >= len(negative_nums):
        result += negative_nums[i]
    else:
        result += (negative_nums[i] * negative_nums[i + 1])

print(result)
