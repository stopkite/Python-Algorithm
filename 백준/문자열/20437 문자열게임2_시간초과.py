import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline()
    k = int(sys.stdin.readline())

    arr = []
    for i in range(len(s)):
        for j in range(len(s)):
            if j >= k and j - i >= k:
                arr.append(s[i:j])

    words = []
    for row in arr:
        count_dict = {}
        for elem in row:
            if elem not in count_dict:
                count_dict[elem] = 1
            else:
                count_dict[elem] += 1

        values = list(count_dict.values())
        if k in values:
            words.append(row)

    if not words:
        print(-1)
    else:
        s1 = len(min(words))
        a = ''
        for i in min(words):
            if min(words).count(i) == k:
                a = k
                break

        s2_arr = []
        for w in words:
            if w[0] == w[-1] and w.count(w[0]) == a:
                s2_arr.append(w)
        s2 = len(max(s2_arr))

        print(s1, s2)
