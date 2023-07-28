m = int(input())

if m >= 12 or m <= 2:
    print("Winter")
elif m >= 9:
    print("Fall")
elif m >= 6:
    print("Summer")
else:
    print("Spring")