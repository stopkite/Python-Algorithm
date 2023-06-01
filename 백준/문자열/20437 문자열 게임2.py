import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline()
    k = int(sys.stdin.readline())

    char_dict = {}
    for i in range(len(s)):
        if s.count(s[i]) >= k:
            if s[i] not in char_dict:
                char_dict[s[i]] = [i]
            else:
                char_dict[s[i]].append(i)

    min_val = len(s)
    max_val = -1
    for char, idx_arr in char_dict.items():
        if len(idx_arr) == k:
            l = idx_arr[-1] - idx_arr[0] + 1
            if l < min_val:
                min_val = l
            if l > max_val:
                max_val = l

        elif len(idx_arr) > k:
            st = 0
            while True:
                ed = st + (k - 1)
                l = idx_arr[ed] - idx_arr[st] + 1

                if l < min_val:
                    min_val = l
                if l > max_val:
                    max_val = l

                if ed == len(idx_arr) - 1:
                    break

                st += 1

    if not char_dict:
        print(-1)
    else:
        print(min_val, max_val)
