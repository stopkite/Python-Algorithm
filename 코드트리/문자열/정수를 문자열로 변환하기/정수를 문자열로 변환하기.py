n = int(input())

sum_val = 0
for _ in range(n):
    num = int(input())
    sum_val += num

str_num = str(sum_val)
print(str_num[1:] + str_num[0])