n = int(input())
satisfied = True

for i in range(2, n):
    if n % i == 0:
        satisfied = False

print('P' if satisfied == True else 'C')
