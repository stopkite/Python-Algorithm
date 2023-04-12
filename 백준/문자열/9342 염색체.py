import re

p = re.compile('^[A-F]?A+F+C+[A-F]?$')
n = int(input())

for _ in range(n):
    if p.match(input()):
        print("Infected!")
    else:
        print("Good")
