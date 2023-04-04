arr = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

s = input()
temp = []
for a in s:
    idx = ord(a) - ord('A')
    temp.append(arr[idx])

result = sum(temp) % 10

if result % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
