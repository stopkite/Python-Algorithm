t = int(input())
for _ in range(t):
    w1, w2 = input().split()
    list1 = sorted(list(w1))
    list2 = sorted(list(w2))
    if list1 == list2:
        print(f"{w1} & {w2} are anagrams.")
    else:
        print(f"{w1} & {w2} are NOT anagrams.")
