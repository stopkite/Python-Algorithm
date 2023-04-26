from itertools import permutations

n = int(input())
k = int(input())
arr = [input() for _ in range(n)]
p_arr = list(permutations(arr, k))

numbers = []
for row in p_arr:
    res = ''
    for elem in row:
        res += elem
    numbers.append(res)

print(len(set(numbers)))
