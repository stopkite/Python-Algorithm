import sys


def check_diff(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


def check_string(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            left_check = check_diff(s, l + 1, r)
            right_check = check_diff(s, l, r - 1)

            if left_check or right_check:
                return 1
            else:
                return 2
    return 0


t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().rstrip()

    l = 0
    r = len(s) - 1

    print(check_string(s, l, r))
