n = int(input())
MAX_NUM = 45
memo = [-1] * (MAX_NUM + 1)


def fib(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]

print(fib(n))
