def solution(book_time):
    times_dict = {}
    for book in book_time:
        st = (int(book[0][:2]) * 60) + int(book[0][3:])
        ed = (int(book[1][:2]) * 60) + int(book[1][3:])
        for t in range(st, ed + 10):
            if t not in times_dict:
                times_dict[t] = 1
            else:
                times_dict[t] += 1

    return max(times_dict.values())
