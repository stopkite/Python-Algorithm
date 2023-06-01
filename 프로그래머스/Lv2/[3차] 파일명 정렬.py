def solution(files):
    answer = []
    file_order = []
    for idx, file in enumerate(files):
        h, n = '', ''
        last_numeric_idx = len(file)
        for i in range(len(file)):
            if not file[i].isnumeric():
                if i < last_numeric_idx:  # head
                    h += file[i]

                if i - 1 == last_numeric_idx:  # tail
                    break

            else:  # number
                n += file[i]
                last_numeric_idx = i

        file_order.append((h, n, idx))

    file_order.sort(key=lambda x: (x[0].upper(), int(x[1])))

    for f in file_order:
        answer.append(files[f[2]])

    return answer
