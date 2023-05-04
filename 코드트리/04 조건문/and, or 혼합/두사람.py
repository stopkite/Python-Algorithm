# 한 사람이라도 19세이상, 남성 -> 1
arr = input().split()
a_age, a_sex = int(arr[0]), arr[1]

arr = input().split()
b_age, b_sex = int(arr[0]), arr[1]

if (a_age >= 19 and a_sex == 'M') or (b_age >= 19 and b_sex == 'M'):
    print(1)
else:
    print(0)