n, m = map(int, input().split())

set_n = set()
for _ in range(n):
    set_n.add(input())

set_m = set()
for _ in range(m):
    set_m.add(input())

result = list(set_n & set_m)
print(len(result))

result.sort()

for elem in result:
    print(elem)
