n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    question_arr = list(map(int, input().split()))

    a = question_arr[1]

    if question_arr[0] == 1:
        print(arr[a - 1])
    elif question_arr[0] == 2:
        print(arr.index(a) + 1 if a in arr else 0)
    else:
        b = question_arr[2]
        for elem in arr[a - 1:b]:
            print(elem, end=" ")
        print()