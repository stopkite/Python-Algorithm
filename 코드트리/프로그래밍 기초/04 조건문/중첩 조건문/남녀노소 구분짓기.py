sex = int(input())
age = int(input())

if sex == 0:
    print("MAN" if age >= 19 else "BOY")
else:
    print("WOMAN" if age >= 19 else "GIRL")