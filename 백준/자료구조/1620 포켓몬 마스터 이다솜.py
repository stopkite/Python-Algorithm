import sys
n, m = map(int, sys.stdin.readline().split())
book = {}

for i in range(n):
    monster = sys.stdin.readline().strip()
    book[i + 1] = monster
    book[monster] = i + 1

for _ in range(m):
    a = sys.stdin.readline().strip()
    if not a.isalpha():
        print(book[int(a)])
    else:
        print(book[a])
