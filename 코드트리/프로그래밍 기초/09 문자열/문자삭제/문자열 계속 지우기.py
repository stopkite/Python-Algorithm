a = input()
b = input()

while a.find(b) != -1:
    start_index = a.find(b)
    a = a[:start_index] + a[start_index+len(b):]

print(a)