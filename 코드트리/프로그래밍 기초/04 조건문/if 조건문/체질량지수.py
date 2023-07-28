arr = input().split()
height, weight = int(arr[0]), int(arr[1])

bmi = (weight * 100 * 100) // (height ** 2)

print(bmi)

if bmi >= 25:
    print("Obesity")
