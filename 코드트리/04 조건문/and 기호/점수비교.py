a = input().split()
a_math, a_eng = int(a[0]), int(a[1])

b = input().split()
b_math, b_eng = int(b[0]), int(b[1])

if a_math > b_math and a_eng > b_eng:
    print(1)
else:
    print(0)